# Personalized Manual Experience

<form id="personalized-form">
    <div style="background-color: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 30px; max-width: 600px; margin: 0 auto;">
        <h2 style="text-align: center; font-size: 1.5rem; margin-bottom: 20px; color: #007bff;">Personalized Manual Experience</h2>

        <!-- Question 1: Are you a PhD student? -->
        <div class="form-group">
            <label for="phdYes">Are you a PhD student?</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="phdStudent" id="phdYes" value="yes" required>
                <label class="form-check-label" for="phdYes">Yes</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="phdStudent" id="phdNo" value="no" required>
                <label class="form-check-label" for="phdNo">No</label>
            </div>
        </div>

        <!-- Question 2: Request research assistants -->
        <div class="form-group hidden" id="researchAssistantsGroup">
            <label>If you are not a PhD student, are you going to request research assistants from VBL?</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="requestAssistants" id="assistantsYes" value="yes">
                <label class="form-check-label" for="assistantsYes">Yes</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="requestAssistants" id="assistantsNo" value="no">
                <label class="form-check-label" for="assistantsNo">No</label>
            </div>
        </div>

        <!-- Question 3: Online or Lab study -->
        <div class="form-group">
            <label>Is your study an online study or a lab study?</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="studyType" id="onlineStudy" value="online" required>
                <label class="form-check-label" for="onlineStudy">Online Study</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="studyType" id="labStudy" value="lab" required>
                <label class="form-check-label" for="labStudy">Lab Study</label>
            </div>
        </div>

        <button type="submit" class="btn" style="background-color: #007bff; color: white; padding: 10px 20px; border-radius: 50px; font-size: 1rem; transition: all 0.3s ease;">Submit</button>
    </div>
</form>

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script>
    $(document).ready(function() {
        // Show/Hide the research assistants question based on PhD student answer
        $('input[name="phdStudent"]').change(function() {
            if ($('#phdNo').is(':checked')) {
                $('#researchAssistantsGroup').removeClass('hidden');
            } else {
                $('#researchAssistantsGroup').addClass('hidden');
                $('input[name="requestAssistants"]').prop('checked', false); // Reset assistant choices
            }
        });
    });
</script>
