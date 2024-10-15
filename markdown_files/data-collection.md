
# Your responsibility during data collection

{% if study_type == 'online' or assistant_status == 'y'%}
As soon as the study details have been approved by us, your study will be launched and advertised to the students.

{% if study_type == 'online'%}
For **your online study**, students can enroll and participate directly, and you do not have a responsibility during data collection.
{% endif %}
{% if assistant_status == 'y' %}
Given that you are requesting lab assistants from us, we will arrange **your lab study** by opening time slots on SONA, and arranging the study in the Transitorium building. You do not have a responsibility during this process.
{% endif %}

Although, we do recommend that you already check out now what needs to be done after data collection by following the next steps, so that you know what to expect. 
{% endif %}

{% if faculty == 'FGB' and study_type == 'lab' %}
As an FGB researcher, it is your responsibility to arrange lab access to the Brain & Behaviour Labs facilities. You can consult the [BBLabs Documentation](https://brainbehavior.labs.vu.nl/docs#/){:target="_blank" rel="noopener noreferrer"}.

If your study includes timeslots that participants can sign up to, you must also arrange them before your study is launched. Once the study is launched, students will enroll in one of the available time slots created by you or your research assistants. Please see the next page on how to **arrange time slots**. 

On the other hand, if your study includes walk-in participation, make sure this is mentioned in the study description.
{% endif %}

{% if faculty == 'SBE' and study_type == 'lab' and assistant_status == 'n' %}
If you are conducting your research on the Transitorium, **we will communicate to you the available dates and times for the lab**. 

Once we do this, you must arrange timeslots that participants can sign up to before your study is launched. Once the study is launched, students will enroll in one of the available time slots created by you. Please see the next page on how to **arrange time slots**. 

It is also your responsibility to arrange lab access to the lab facilities. After the dates of your research have been set, you can arrange access to the building. The next pages give you more information on this.
{% endif %}
