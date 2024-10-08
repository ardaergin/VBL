
# Detailed description

For this section, you can **copy-paste the texts below**. Adjust the empty fields `{...}` according to your study.

If you would like to add more information about your study, you can do so, but please **do not include any information about your hypotheses, variables, or payment**. 


{% if study_type == 'online' %}
>[!info] <i class="fa-solid fa-info"></i> &nbsp Text to copy paste (for an online study)
><br>
>This study will take approximately `{...}` minutes. Payments will only be allocated when you carefully read instructions of the researchers.
>  
>The session is organized by researchers from the Department of `{...}`, Vrije University Amsterdam, `{(if applicable) in collaboration with researchers from ...}`.


{% endif %}
{% if study_type == 'lab' %}
{% if faculty == 'SBE' %}
>[!info] <i class="fa-solid fa-info"></i> &nbsp Text to copy paste (for a physical lab study)
><br>
>This study will take approximately `{...}` minutes. Payments will only be allocated when you carefully read instructions of the researchers.   
>  
>This research takes place in the Applied Behavioural Science Lab, located on the second basement level (-2) of the [Transitorium Building](https://vu.nl/en/about-vu/more-about/transitorium).   
>  
>You must register for a spot in the available time slots. We would like to ask you to be present in the waiting area at least 5 minutes in advance. The waiting room (K1B74) is on the first basement level (-1). The session starts right on time and access to the lab after start time will be denied.   
>
>You can see your Sona ID in your Sona account or in the confirmation email (it is a 5-digit number and it is NOT your Student ID).
>  
>The session is organized by researchers from the Department of {...}, Vrije University Amsterdam, {(if applicable) in collaboration with researchers from ...}.


{% endif %}
{% if faculty == 'FGB' %}
As a researcher from FMG, you need to arrange the labs in the FMG yourself. 
If you will be using the Brain & Behaviour Labs facilities, please consult the 
[BBLabs Documentation](https://brainbehavior.labs.vu.nl/docs#/){:target="_blank" rel="noopener noreferrer"}.

Importantly, if your experiment is a **walk-in study**, start the description with the word “walk-in” and describe when and where students can show up to participate in your study.

>[!info] <i class="fa-solid fa-info"></i> &nbsp Text to copy paste (for a physical lab study)
><br>
>Walk-in `{is / is not}` possible.
> 
>This study will take approximately `{...}` minutes. Payments will only be allocated when you carefully read instructions of the researchers.   
>  
>This research takes place in `{...}`.
>  
>You can also register for a spot in the available time slots.
>
>You can see your Sona ID in your Sona account or in the confirmation email (it is a 5-digit number and it is NOT your Student ID)
>  
>The session is organized by researchers from the Department of `{...}`, Vrije University Amsterdam, `{(if applicable) in collaboration with researchers from ...}`.


{% endif %}
{% endif %}