// Load selections from sessionStorage when the page loads
document.addEventListener('DOMContentLoaded', function () {
    // Load saved selections from sessionStorage
    faculty = sessionStorage.getItem('faculty') || '';
    studyType = sessionStorage.getItem('studyType') || '';
    assistantStatus = sessionStorage.getItem('assistantStatus') || '';

    // If there are saved selections, update the display
    if (faculty) {
        handleFacultySelection(faculty, true); // Second parameter indicates it's a pre-loaded value
    }

    if (studyType) {
        handleStudyType(studyType, true);
    }

    if (assistantStatus && faculty !== 'FGB') { // Only set assistant status if it's not FGB
        handleAssistants(assistantStatus, true);
    }
});

function updateSelections() {
    const selectionsRow = document.getElementById('selectedTags');
    selectionsRow.innerHTML = ''; // Clear previous selections

    // Only add the faculty and study type to the selections
    if (faculty) {
        const facultyTag = createSelectionTag(faculty);
        selectionsRow.appendChild(facultyTag);
    }
    if (studyType) {
        const studyTag = createSelectionTag(studyType);
        selectionsRow.appendChild(studyTag);
    }

    // Only add assistant status if it was explicitly selected by the user (i.e., not auto-set for FGB)
    if (assistantStatus && faculty !== 'FGB') {
        const assistantTag = createSelectionTag(assistantStatus);
        selectionsRow.appendChild(assistantTag);
    }

    // Reveal selections row if there are selections
    if (faculty || studyType || assistantStatus) {
        document.getElementById('selectionsRow').classList.remove('hidden');
        document.getElementById('changeSelectionBtn').classList.remove('hidden'); // Show the change selection button
    } else {
        document.getElementById('selectionsRow').classList.add('hidden');
        document.getElementById('changeSelectionBtn').classList.add('hidden'); // Hide the change selection button
    }
}

function createSelectionTag(label) {
    const tag = document.createElement('span');
    tag.classList.add('badge', 'badge-primary', 'mr-2', 'p-2');

    // Format labels to be more user-friendly
    switch (label) {
        case 'n':
            tag.innerText = 'Conduct Study Yourself';
            break;
        case 'y':
            tag.innerText = 'Request Assistants';
            break;
        default:
            tag.innerText = label;
    }

    return tag;
}


function handleFacultySelection(selectedFaculty, isPreloaded = false) {
    faculty = selectedFaculty;
    if (!isPreloaded) {
        sessionStorage.setItem('faculty', faculty); // Save to sessionStorage if it's a user action
    }

    // Reset button styles
    document.getElementById('facultyFGB').classList.remove('btn-primary');
    document.getElementById('facultyFGB').classList.add('btn-outline-primary');
    document.getElementById('facultySBE').classList.remove('btn-primary');
    document.getElementById('facultySBE').classList.add('btn-outline-primary');

    // Highlight the chosen button
    if (selectedFaculty === 'FGB') {
        document.getElementById('facultyFGB').classList.add('btn-primary');
        document.getElementById('facultyFGB').classList.remove('btn-outline-primary');
    } else if (selectedFaculty === 'SBE') {
        document.getElementById('facultySBE').classList.add('btn-primary');
        document.getElementById('facultySBE').classList.remove('btn-outline-primary');
    }

    // Hide the faculty question and show the study type question
    document.getElementById('facultyQuestion').classList.add('hidden');
    document.getElementById('studyTypeQuestion').classList.remove('hidden');
    updateSelections();  // Update selection display
}

function handleStudyType(type, isPreloaded = false) {
    studyType = type;
    if (!isPreloaded) {
        sessionStorage.setItem('studyType', studyType); // Save to sessionStorage if it's a user action
    }

    // Reset button styles
    document.getElementById('studyOnline').classList.remove('btn-primary');
    document.getElementById('studyOnline').classList.add('btn-outline-primary');
    document.getElementById('studyLab').classList.remove('btn-primary');
    document.getElementById('studyLab').classList.add('btn-outline-primary');

    // Highlight the chosen button
    if (type === 'Online Study') {
        document.getElementById('studyOnline').classList.add('btn-primary');
        document.getElementById('studyOnline').classList.remove('btn-outline-primary');
        document.getElementById('studyTypeQuestion').classList.add('hidden');
        document.getElementById('studySteps').classList.remove('hidden');
        assistantStatus = ''; // Clear assistant status for online studies
        updateLinks();  // Now call updateLinks here
    } else if (type === 'Lab Study') {
        document.getElementById('studyLab').classList.add('btn-primary');
        document.getElementById('studyLab').classList.remove('btn-outline-primary');
        document.getElementById('studyTypeQuestion').classList.add('hidden');
        if (faculty !== 'FGB') {
            // Show the assistant question if it's not FGB
            document.getElementById('nextQuestion').classList.remove('hidden');
        } else {
            // Automatically set the assistant status for FGB and display the steps
            assistantStatus = 'n'; // Set to 'n' for Conduct Study Yourself
            sessionStorage.setItem('assistantStatus', assistantStatus);
            document.getElementById('studySteps').classList.remove('hidden'); // Show the steps for FGB Lab Study
            updateLinks(); // Ensure the links are updated correctly for FGB Lab Study
        }
    }

    updateSelections();  // Update selection display
}


function handleAssistants(status, isPreloaded = false) {
    assistantStatus = status;
    if (!isPreloaded) {
        sessionStorage.setItem('assistantStatus', assistantStatus); // Save to sessionStorage if it's a user action
    }

    // Reset button styles
    document.getElementById('assistYes').classList.remove('btn-success');
    document.getElementById('assistYes').classList.add('btn-outline-success');
    document.getElementById('assistNo').classList.remove('btn-success');
    document.getElementById('assistNo').classList.add('btn-outline-success');

    // Highlight the chosen button
    if (status === 'Request Assistants') {
        document.getElementById('assistYes').classList.add('btn-success');
        document.getElementById('assistYes').classList.remove('btn-outline-success');
    } else if (status === 'Conduct Study Yourself') {
        document.getElementById('assistNo').classList.add('btn-success');
        document.getElementById('assistNo').classList.remove('btn-outline-success');
    }

    document.getElementById('nextQuestion').classList.add('hidden');
    document.getElementById('studySteps').classList.remove('hidden');
    updateSelections();  // Update selection display
    updateLinks();
}

function updateLinks() {
    let studyPath = '';

    if (studyType === 'Online Study') {
        // Online Study doesn't need the assistant status, but we add '/n/' as a placeholder
        studyPath = `${faculty}/online/n`;
    } else {
        // Lab study logic
        if (faculty === 'FGB') {
            // For FGB, automatically set the assistant status to 'n' and do not show it in the display
            studyPath = `${faculty}/lab/n`;
        } else {
            // For other faculties, respect the chosen assistant status
            studyPath = `${faculty}/lab`;
            studyPath += assistantStatus === 'Conduct Study Yourself' ? '/n' : '/y';
        }
    }

    // Update the links with the correct path
    document.getElementById('step1Link').href = `/step-1/${studyPath}/step-1-overview`;
    document.getElementById('step2Link').href = `/step-2/${studyPath}/step-2-overview`;

    console.log("Generated Links: ", {
        step1: `/step-1/${studyPath}/step-1-overview`,
        step2: `/step-2/${studyPath}/step-2-overview`
    });
}



function resetSelections() {
    faculty = '';
    studyType = '';
    assistantStatus = '';  // Reset this variable as well

    // Clear sessionStorage
    sessionStorage.removeItem('faculty');
    sessionStorage.removeItem('studyType');
    sessionStorage.removeItem('assistantStatus');

    // Hide the selections row and change button
    document.getElementById('selectionsRow').classList.add('hidden');
    document.getElementById('changeSelectionBtn').classList.add('hidden');

    // Clear previous selections
    document.getElementById('selectedTags').innerHTML = '';

    // Show the first question again
    document.getElementById('facultyQuestion').classList.remove('hidden');
    document.getElementById('studyTypeQuestion').classList.add('hidden');
    document.getElementById('nextQuestion').classList.add('hidden');
    document.getElementById('studySteps').classList.add('hidden');

    // Reset button styles
    resetButtonStyles();
}

function resetButtonStyles() {
    document.getElementById('facultyFGB').classList.remove('btn-primary');
    document.getElementById('facultyFGB').classList.add('btn-outline-primary');
    document.getElementById('facultySBE').classList.remove('btn-primary');
    document.getElementById('facultySBE').classList.add('btn-outline-primary');

    document.getElementById('studyOnline').classList.remove('btn-primary');
    document.getElementById('studyOnline').classList.add('btn-outline-primary');
    document.getElementById('studyLab').classList.remove('btn-primary');
    document.getElementById('studyLab').classList.add('btn-outline-primary');

    document.getElementById('assistYes').classList.remove('btn-success');
    document.getElementById('assistYes').classList.add('btn-outline-success');
    document.getElementById('assistNo').classList.remove('btn-success');
    document.getElementById('assistNo').classList.add('btn-outline-success');
}
