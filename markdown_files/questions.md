<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Manual Experience</title>
    <!-- Bootstrap for modern styles -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <style>
        /* Custom Styles */
        body {
            font-family: 'Montserrat', sans-serif;
            background-color: #f8f9fa;
            padding: 30px;
        }

        .form-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 30px;
            max-width: 600px;
            margin: 0 auto;
        }

        .form-header {
            text-align: center;
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: #007bff;
        }

        .form-group label {
            font-weight: bold;
        }

        .btn-custom {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border-radius: 50px;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .btn-custom:hover {
            background-color: #0056b3;
        }

        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2 class="form-header">Personalized Manual Experience</h2>
        <form id="personalized-form">

            <!-- Question 3: Is your study an online study or a lab study? -->
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
            <!-- Question 1: Are you a PhD student? -->
            <div class="form-group">
                <label>Are you a PhD student?</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="phdStudent" id="phdYes" value="yes" required>
                    <label class="form-check-label" for="phdYes">Yes</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="phdStudent" id="phdNo" value="no" required>
                    <label class="form-check-label" for="phdNo">No</label>
                </div>
            </div>

            <!-- Question 2: If not, request research assistants -->
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

            

            <button type="submit" class="btn btn-custom">Submit</button>
        </form>
    </div>

    <!-- jQuery for form handling -->
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
</body>
</html>
