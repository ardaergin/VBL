
# What to do on a study day

On the day of your studies, once you or the assistants are in the lab, check each student using the dashboard section of your study.

Follow the steps below to set up the lab before the session:

<div class="checklist-container">
    <ul class="styled-checklist">
        <li><input type="checkbox" id="step1"> Log in to the main computer</li>
        <li><input type="checkbox" id="step2"> Place the survey link in the "Start Here" folder</li>
        <li><input type="checkbox" id="step3"> Log in to all cubicle computers</li>
        <li><input type="checkbox" id="step4"> Ensure all computers have the study link open in full-screen mode</li>
    </ul>
</div>
<button class="reset-btn" onclick="resetChecklist()">Reset Checklist</button>
<style>
/* Checklist Container */
.checklist-container {
    background: #f9f9f9;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

/* Styled List */
.styled-checklist {
    list-style: none;
    padding: 0;
}

.styled-checklist li {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    font-size: 1.1em;
}

/* Customize Checkboxes */
.styled-checklist input[type="checkbox"] {
    width: 20px;
    height: 20px;
    margin-right: 10px;
    cursor: pointer;
    accent-color: #007bff; /* Blue accent for checkboxes */
}

/* Button to Reset Checklist */
.reset-btn {
    display: inline-block;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 15px;
    cursor: pointer;
    font-size: 1em;
    margin-top: 10px;
    transition: background-color 0.3s;
}

.reset-btn:hover {
    background-color: #0056b3;
}
</style>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const checkboxes = document.querySelectorAll('.styled-checklist input[type="checkbox"]');
        
        // Load saved state from localStorage
        checkboxes.forEach(checkbox => {
            checkbox.checked = localStorage.getItem(checkbox.id) === 'true';
            checkbox.addEventListener('change', () => {
                localStorage.setItem(checkbox.id, checkbox.checked);
            });
        });
    });

    function resetChecklist() {
        const checkboxes = document.querySelectorAll('.styled-checklist input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
            localStorage.removeItem(checkbox.id);
        });
    }
</script>


### Setting up the lab
Arrive at the lab about 30-45 minutes in advance, and set up all computers. 

- Log in to the main computer (you will have been provided the login credentials prior to your experiment).
- Place the link to your survey as a shortcut to the folder named "Start Here" on the desktop on the computer, it will automatically be on all other desktops. 
- Turn on the other computers inside the cubicles, and login with the same credentials. 
- You should see the folder in all other computers through which you can access the study link. 
- Ensure the study link is opened on each computer (click on the link and press F11 to have a full screen mode).

>[!screenshot] <i class="fa-solid fa-camera"></i> &nbsp Screenshot: The folder in the lab computer desktop
><img src="/static/images/desktop.png" alt="Desktop" class="responsive-image">


### Starting your study sessions

1. Pick up the participants from the waiting room (-1 Floor of the Transitorium building).
    - Call their attention/opening: "Are you here for the `[Time]` session of the `[Experiment Name]`? 
    - Then, bring them to the lab. 
2. After all the participants are downstairs, mark them as participated/unexcused.
    - Read outloud the SONA IDs you have for the current timeslot, and ask students to identify themselves. 
    - Mark them as participated or unexcused. Please see the [granting or denying payment page](granting-or-denying-payment) to learn how to do that.
3. Give instructions to all students.
    - Standard Instructions: "Thank you for your participation! Please leave your bags and phones outside. Hand your coats on the coat hangers available. This study will take about `[your study duration]` minutes, and it `[consists of a single study / several independent studies]`. Please read everything carefully and answer all the required questions. Please also prepare your research ID (a 4/5-digit number). When there is no way to continue to the next page, it’s finished. Now you can enter a cubicle."

Commonly asked questions by participants:

- **"Can I switch sessions?"** or **"I am late, can I participate in the next session?"**: This type of request is usually not encouraged. However, if there are available timeslots in the next session and you feel comfortable to accommodate the request, you can do so. We recommend you to take a note of such situations for yourself for recordkeeping purposes.
- **"My computer crashed!"**: If there is an available cubicle, take the participant there. If there are not enough computers due to emergent issues, take a note of the participant's ID, and let them go. The participant will receive payment for their participation regardless. Report the issue asap to VBL (vbl@vu.nl) and the Lab manager (s.desikan@vu.nl). 

### Ending your study sessions
It is important to note that you put the things in the lab as they were before. 

- Switch off all computers.
- All keyboards, mouse, headphones and chairs should be placed as you found them. 
- Turn off the lights, close the door, and check if it is locked.
- Return your access cards to the HOST of the Transitorium building.
