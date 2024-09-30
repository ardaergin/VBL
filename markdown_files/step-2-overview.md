{% if study_type == 'online' %}
# Your responsibility during data collection

As soon as the requested details have been approved by us, the study will be launched and advertised to the students.

For your **online study**, students can enroll and participate directly, and you do not have a responsibility during data collection.

Although, we do recommend that you check out now what needs to be done in Step 3 (i.e., "after data collection"), so that you know what to expect. 
{% endif %}

{% if study_type == 'lab' %}
{% if assistant_status == 'n' %}
# Step 2 Overview

In this step, you will arrange your lab study by opening time slots on SONA, and arranging access to the Transitorium building. You will also learn about what to do on the day of your studies. 
{% endif %}

{% if assistant_status == 'y' %}
# Your responsibility during data collection

As soon as the requested details have been approved by us, the study will be launched and advertised to the students.

Given that you are requesting student assistants from us, we will arrange your lab study by opening time slots on SONA, and arranging the study in the Transitorium building. You do not have a responsibility during this process

Although, we do recommend that you check out now what needs to be done in Step 3 (i.e., "after data collection"), so that you know what to expect. 
{% endif %}

{% endif %}
