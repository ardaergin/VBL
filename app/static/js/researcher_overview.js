let faculty = '';
let studyType = '';
let assistantStatus = '';  // Updated variable

function updateSelections() {
    const selectionsRow = document.getElementById('selectedTags');
    selectionsRow.innerHTML = ''; // Clear previous selections

    if (faculty) {
        const facultyTag = createSelectionTag(faculty);
        selectionsRow.appendChild(facultyTag);
    }
    if (studyType) {
        const studyTag = createSelectionTag(studyType);
        selectionsRow.appendChild(studyTag);
    }
    if (assistantStatus) {
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
    tag.innerText = label;
    return tag;
}

function handleFacultySelection(selectedFaculty) {
    faculty = selectedFaculty;

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

function handleStudyType(type) {
    studyType = type;

    // Reset button styles
    document.getElementById('studyOnline').classList.remove('btn-primary');
    document.getElementById('studyOnline').classList.add('btn-outline-primary');
    document.getElementById('studyLab').classList.remove('btn-primary');
    document.getElementById('studyLab').classList.add('btn-outline-primary');

    // Highlight the chosen button
    if (type === 'Online Study') {
        console.log('Online Study selected');  // Debugging
        document.getElementById('studyOnline').classList.add('btn-primary');
        document.getElementById('studyOnline').classList.remove('btn-outline-primary');

        // Hide the study type question and reveal study steps immediately
        document.getElementById('studyTypeQuestion').classList.add('hidden');
        document.getElementById('studySteps').classList.remove('hidden');
        assistantStatus = ''; // Clear assistant status for online studies
        updateLinks();  // Now call updateLinks here
    } else if (type === 'Lab Study') {
        console.log('Lab Study selected');  // Debugging
        document.getElementById('studyLab').classList.add('btn-primary');
        document.getElementById('studyLab').classList.remove('btn-outline-primary');

        // Hide the study type question and show the next question (Request Assistants)
        document.getElementById('studyTypeQuestion').classList.add('hidden');
        document.getElementById('nextQuestion').classList.remove('hidden');
    }

    updateSelections();  // Update selection display
}

function handleAssistants(status) {
    assistantStatus = status;

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

    // Hide Assistants question and reveal study steps
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
        // Lab study needs all three selections (faculty, study type, assistant status)
        studyPath = `${faculty}/lab`;
        studyPath += assistantStatus === 'Conduct Study Yourself' ? '/n' : '/y';
    }

    // Update the links with the correct path
    document.getElementById('step1Link').href = `/step-1/${studyPath}/step-1-overview`;
    document.getElementById('step2Link').href = `/step-2/${studyPath}/step-2-overview`;
    document.getElementById('step3Link').href = `/step-3/${studyPath}/step-3-overview`;

    console.log("Generated Links: ", {
        step1: `/step-1/${studyPath}/step-1-overview`,
        step2: `/step-2/${studyPath}/step-2-overview`,
        step3: `/step-3/${studyPath}/step-3-overview`
    });
}

// Reset all selections when the user clicks "Change Selection"
function resetSelections() {
    faculty = '';
    studyType = '';
    assistantStatus = '';  // Reset this variable as well

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
