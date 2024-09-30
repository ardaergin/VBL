
# Detailed description

{% if faculty == 'FGB' %}
Provide a description of about 30 words of the experiment. This description should be simple, but informative (e.g., this experiment explores whether personality is related to memory performance). 

Make these descriptions informative so that potential participants can make an informed choice about participating in the experiment.

If your experiment is a **walk-in study**, start the description with the word “walk-in” and describe when and where students can show up to participate in your study.

>[!info] <i class="fa-solid fa-info"></i> &nbsp Text to Copy Paste (Physical Lab Study)
><br>
> This study will take approximately {...} minutes. Payments will only be allocated when you carefully read instructions of the researchers.   
>  
> This research takes place in {...}. 
>
> Walk-in {is / is not} possible.
>  
> You can register for a spot in the available time slots. We would like to ask you to be present in the waiting area at least 5 minutes in advance. The waiting room (K1B74) is on the first basement level (-1). The session starts right on time and access to the lab after start time will be denied.   
>
> You can see your Sona ID in your Sona account or in the confirmation email (it is a 5-digit number and it is NOT your Student ID)
>  
> The session is organized by researchers from the Department of {...}, Vrije University Amsterdam, {*(if applicable)* in collaboration with researchers from ...}.     
>  
> If you would like to have more information about the study, you can contact the researchers through "Study Information".

{% endif %}



{% if faculty == 'SBE' %}
For this section, you can **copy-paste one of the texts below**. Adjust the empty fields `{...}` according to your study.

If you would like to add more information for the participants, you can do so, but please **do not include any information about your hypotheses or variables**. 

{% if study_type == 'online' %}
>[!info] <i class="fa-solid fa-info"></i> &nbsp Text to Copy Paste (Online Study)
><br>
> This study will take approximately {...} minutes. Payments will only be allocated when you carefully read instructions of the researchers.
>  
> The session is organized by researchers from the Department of {...}, Vrije University Amsterdam, {*(if applicable)* in collaboration with researchers from ...}.     
> 
> If you would like to have more information about the study, you can contact the researchers through "Study Information".
{% endif %}

{% if study_type == 'lab' %}
>[!info] <i class="fa-solid fa-info"></i> &nbsp Text to Copy Paste (Physical Lab Study)
><br>
> This study will take approximately {...} minutes. Payments will only be allocated when you carefully read instructions of the researchers.   
>  
> This research takes place in the Applied Behavioural Science Lab, located on the second basement level (-2) of the [Transitorium Building](https://vu.nl/en/about-vu/more-about/transitorium).   
>  
> You must register for a spot in the available time slots. We would like to ask you to be present in the waiting area at least 5 minutes in advance. The waiting room (K1B74) is on the first basement level (-1). The session starts right on time and access to the lab after start time will be denied.   
>
> You can see your Sona ID in your Sona account or in the confirmation email (it is a 5-digit number and it is NOT your Student ID)
>  
> The session is organized by researchers from the Department of {...}, Vrije University Amsterdam, {*(if applicable)* in collaboration with researchers from ...}.     
>  
> If you would like to have more information about the study, you can contact the researchers through "Study Information".
{% endif %}
{% endif %}

