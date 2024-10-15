
# Submitting your study for approval

Once you have your study ready, you can submit your study for approval. 

{% if faculty == 'SBE'%}
{% if assistant_status == 'y'%}
**We strongly recommend testing your design** before requesting for approval. We are happy provide access to the lab facilities to test your study.
{%endif%}

1. In "My Studies," click "Inactive," select your study, and under "Study Information," click "Send Request."
2. On this new page, in the text box, include your **faculty**, **budget number**, **desired number of participants**, **desired completion date**. {% if study_type == 'lab' %} Given that you have a lab study, please indicate whether you need our research assistants or will bring your own (note that PhD students must conduct their studies themselves).{% endif %} See below for an example entry to this text box.
{% if assistant_status == 'y' %}
3. Since you are requesting lab assistants from us, please attach **a Word/PDF document with the instructions** necessary to carry out your study. These instructions will be used by our lab assistants.
{% endif %} 
4. Once everything is complete, click the "**Send Request**" button.
5. Finally, we also would like you to share your survey with us. For instance, if you are using Qualtrics, please add [vbl@vu.nl](mailto:vbl@vu.nl) to the collaborators of the study under "add the people you want to collaborate with". If you are running a study that cannot be collaborated online, please email us. 

>[!info] <i class="fa-solid fa-info"></i> &nbsp Example Text Box Submission
><pre style="font-size: 16px; color: rgba(51, 51, 51, 1); padding: 15px; border-radius: 5px; white-space: pre-wrap">
> Faculty: SBE
> Desired number of participants: 200 
> Desired completion date: 15 November 2024
> Budget number ("WBS element"): D/464170.891
{% if assistant_status == 'y' %}
> Request for research assistants: yes 
{%endif%}
> </pre>
{%endif%}

{% if faculty == 'FGB'%}
1. In "My Studies," click "Inactive," select your study, and under "Study Information," click "Send Request."
2. On this new page, in the text box, include your **faculty**, **budget number**, and **desired number of participants**. See below for an example entry to this text box.
3. Once everything is complete, click the "**Send Request**" button.
4. Finally, we also would like you to share your survey with us. For instance, if you are using Qualtrics, please add [vbl@vu.nl](mailto:vbl@vu.nl) to the collaborators of the study under "add the people you want to collaborate with". If you are running a study that cannot be collaborated online, please email us. 

>[!info] <i class="fa-solid fa-info"></i> &nbsp Example Text Box Submission
><pre style="font-size: 16px; color: rgba(51, 51, 51, 1); padding: 15px; border-radius: 5px; white-space: pre-wrap">
> Faculty: FGB
> Budget number ("WBS element"): D/464170.891
> Desired number of participants: 200
> </pre>

{%endif%}
