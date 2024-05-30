
# VBL Repository

This repository is developed for VU Behavioral Lab (VBL). 

The VU Behavioural Lab (VBL) is interdisciplinary and consists of several laboratories from different disciplines – bringing together scholars from behavioural economics, psychology, organizational behaviour, marketing, public administration, law, and communication. It is designed to integrate, professionalize, and expand the facilities for behavioural experimental research, in order to stimulate research and collaborations, and to improve visibility.

VBL is geared towards addressing insufficient lab resources in many faculties, with a focus on enhancing research productivity by providing necessary facilities and services. Furthermore, VBL aims to establish a centralized digital platform, streamline lab efficiency, improve visibility, and strengthen VU's competitive position by being an attractive employer for top-tier behavioural researchers.

In pursuit of these goals, VBL provides researchers with a diverse array of resources, encompassing various types of specialized lab spaces, an active participant pool, and cutting-edge software and hardware. Additionally, we facilitate the collaboration and knowledge exchange of behavioural researchers from VU Amsterdam, fostering the creation of a network within the community.


# Some Debugging Tips
If you run into a problem with "segmentation fault", when running the app: 

- downgrade torch to `2.0.1`.
- run `OMP_NUM_THREADS=1` on the command line (Mac/Linux).
- run `KMP_DUPLICATE_LIB_OK=TRUE` on the command line (Mac/Linux).
