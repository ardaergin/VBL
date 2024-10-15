
# Granting or denying payment

As your study is running, it is your responsibility to keep the list of participants that need to be paid up to date.

The system will automatically send the list of participants of your study that have participated the week before and are not marked as "no-show" to the financial department **every Tuesday at 23:59**.

For instance, if a participant participated in your study on October 2nd, Wednesday, and marked as "participated", their financial information will be automatically sent to the financial department on October 8th, Tuesday at 23:59.

This process is regardless whether your study is completed, since some studies take long durations of time, and participants need to be paid periodically.

Hence, it is your responsibility to make any changes to the list of participants that need to be paid. If you have not made any changes, all the participants will be paid, even if they are marked as "no action taken", and might not have participated in your study. 

>[!info] <i class="fa-solid fa-info"></i> &nbsp How to navigate to the payment page on SONA 
>
>1. In SONA, locate and click on **'My Studies'**. This will take you to a list of all your posted studies. 
>2. Among your studies, find the specific study for which you want to grant or deny payments and click on it. This action will display the study's details.
>3. Under the study details, click on **'View/Administer Time slots'**. You will see a display showing the current schedule and time slots for the study.
>3. To grant or deny payment for a specific time slot, click on **'Modify'** next to that time slot.
>4. Here, within the **'Sign-Ups' section**, you'll find a table listing the participants scheduled for that time slot.
>5. Grant or deny payment based on the instructions below.
>6. Carefully check that no students are left with the status "No action taken". You can check these in the tab **"Uncredited sign-ups"**
>7. After making your selections for each participant, scroll down to the bottom of the table and make sure to click on the **'Update Sign-Ups'** button to register the granted or denied credits into the system.

{% if study_type == 'online' %}
For online studies, participants are marked as "participated" automatically when they complete your study. Nevertheless, you still have actions to take.

First, sometimes participants sign up to participate but do not end up participating. In these cases, you should select "Excused" under "No-Show" instead. The participant will be denied payments, but will not receive any penalty.

Secondly, you should check your data, and deny payment if necessary. Please see below for the conditions under which you can deny payment and how to do so.
{% endif %}

>[!info] <i class="fa-solid fa-info"></i> &nbsp Do you have an incentivized study? 
><br>
> For incentivized studies, you can also arrange the incentive payment through the payment page on SONA. 
>
> Example: 
> 
> - You have a performance task in your research and you incentivize participants by paying 15 EUR for the top 10 best performing participants.
> - After your study is concluded, you identify the top 10. 
> - On the payment page on SONA (same page as described above), for each of these 10 participants, you should enter "Incentive: 15" as a comment. 
> - We will make the payment according to these comments, hence, please do not deviate from the format of "Incentive: `{amount}`".

{% if study_type == 'lab' and assistant_status == 'y' %}
Given that you have requested lab assistants from us, they will mark participants as "participated" or “no-show”. Hence, your only task is to investigate your data, and deny payment if necessary. Please see below for the conditions under which you can deny payment and how to do so.
{% endif %}

{% if study_type == 'lab' and assistant_status == 'n' %}
Given that you are conducting your lab study yourself, you must mark "participated" or "no-show" yourself. For a smoother process, these two should be carried out as the study is ongoing.

- Participant participated > "Participated"
- Participant no-show, contacted you on time > **"Excused No-Show"**
- Participant no-show, *did not* contact you on time > **'Unexcused No-Show'**

After the study has been completed, you can deny payment if necessary.
{% endif %}

## Denying payment

You should investigate your data and deny the payment when necessary.

### Conditions under which you can deny payment
- The participant **did not give consent**, and, therefore, did not participate in the study.
- The participant **did not finish** the study. You cannot deny payment if the participant skipped questions but finalized the study.
- The participant failed an **attention check**.
- The participant completed the task at an **unusually rapid pace**, identified as being more than 3 standard deviations faster than the average.
- The participant **clearly did not show effort** for the study, even though you have *explicitly specified* the amount of effort you are expecting. For example, when explicitly asked to write a paragraph, they only wrote a couple of words, or for the entire survey, they chose the same point on a Likert scale.

### How to deny payment
To deny payment to a participant, because of any of these conditions, keep their status as "participated", but add a comment "Payment denied: `{...}`" with filling in the `{...}` field with the appropriate reasoning (e.g., "failed attention check"). This comment will be visible to the students. Please do not deviate from the wording "Payment denied" at the beginning of the comment. You HAVE TO add such comments if you would like to deny payment.

