
# Payment

The payment for the studies are calculated based on:

- 10€ per hour for physical lab studies.
- 7.5€ per hour for online studies. 

You can use the tool below to calculate the amount you have to pay each participant based on the [duration](duration) of your study (in minutes).

<div>
    <input type="range" id="timeSlider" name="timeSlider" min="0" max="120" value="0" oninput="updateAmount()">
    <span id="timeDisplay">0</span> minutes
</div>
<div>
    <p>Online study: <span id="onlineAmount">€0.00</span></p>
    <p>Physical study: <span id="physicalAmount">€0.00</span></p>
</div>

---

**Do you have an incentivized study?** You can pay different participants different amounts. This can be arranged after the study is conducted. Please see the page for [granting or denying payment](granting-or-denying-payment). For the current payment field in the study description, simply enter the usual amount (i.e., incentive not included). 
