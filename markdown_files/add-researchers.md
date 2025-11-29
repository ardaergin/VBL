---
name: "Add researchers"
---

# Adding researchers to your study

Here you select **your name** as a researcher, and add your **co-authors** if there are any. Note that you can only add VU employees or students. 

If they are not yet registered as researcher in SONA, they have to email us at <a href="mailto:vbl@vu.nl">vbl@vu.nl</a> with the following details:
        <ul>
            <li>First Name</li>
            <li>Last Name</li>
            <li>VUnet ID</li>
            <li>VU Email Address</li>


{% if study_type == 'lab' %}

{% if assistant_status == 'n' %}
Given that you are conducting the lab study yourself, or with your own research assistants, your research assistants need to be added as a researcher to your study, in order to manage the time slots and payment. For them to be added as a researcher to the study, they must have an account on VBL SONA. Hence, please ask your research assistant(s) to request an account by emailing us at [vbl@vu.nl](mailto:vbl@vu.nl) with their (1) first name, (2) last name, (3) VUnet ID, and (4) VU email address.
{% endif %}

{% if assistant_status == 'y' %}
Given that you are going to request lab assistants from VBL for your physical study, we will also add the available VBL research assistants to your study for them to manage the time slots and payment.
{% endif %}

{% endif %}

