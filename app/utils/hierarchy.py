page_hierarchy = {
    "home": 0,

    "contact": {
        "parent": "home", 
        "display": "Contact"
        },
    "facilities": {
        "parent": "home", 
        "display": "Facilities at VBL"
        },
    "faq-for-researchers": {
        "parent": "home", 
        "display": "FAQ for Researchers"
        },
    "faq-for-students": {
        "parent": "home", 
        "display": "FAQ for Students"
        },
    

    ##### STUDENTS #####
    "how-to-participate": {
        "parent": "home", 
        "display": "How to Participate"
        },

    

    ##### RESEARCHERS #####
    "researcher-overview": {
        "parent": "home", 
        "display": "Researcher manual"
        },

        "create-a-new-study": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Create a New Study"
            },
            "select-the-study-type": {
                "parent": "create-a-new-study", 
                "display": "Select the Study Type"
                },
                
            "fill-in-the-study-information": {
                "parent": "create-a-new-study", 
                "display": "Fill in the Study Information"
                },

                "study-name": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Study Name"
                    },
                "brief-abstract": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Brief Abstract"
                    },
                "detailed-description": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Detailed Description"
                    },
                "eligibility-requirements": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Eligibility Requirements"
                    },
                "duration": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Duration"
                    },
                "payment": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Payment"
                    },
                "preparation": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Preparation"
                    },
                "add-researchers": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Adding Researchers to Your Study"
                    },
                "ethical-approval": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Ethical Approval"
                    },

        "submission-for-approval": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Submitting Your Study for Approval"
            },

        "attention-checks": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Attention Checks"
            },
        
        "arranging-lab-study-yourself": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Arranging a Physical Study Yourself"
            },

            "arranging-time-slots": {
                "parent": "arranging-lab-study-yourself", 
                "display": "Arranging Time Slots on SONA"
                },

        "responsibility-during-data-collection": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Responsibility During the Data Collection"
            },
        
        "granting-or-denying-payment": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Granting or Denying Payment"
            },

            "denying-payment": {
                "parent": "granting-or-denying-payment", 
                "display": "Denying Payment"
                },
            
}

def build_full_breadcrumb_path(page_hierarchy):
    full_paths = {}

    def build_path(page_name):
        # Base case: if this page is the "home" page or has no parent defined
        if page_hierarchy[page_name] == 0:
            return [{"name": "home", "display": "Home"}]

        page_info = page_hierarchy[page_name]
        parent_path = build_path(page_info["parent"]) if page_info["parent"] in page_hierarchy else []
        current_page_path = {"name": page_name, "display": page_info["display"]}
        return parent_path + [current_page_path]

    for page in page_hierarchy:
        full_paths[page] = build_path(page)

    return full_paths

# Transform the simplified hierarchy into the full breadcrumb paths
full_page_hierarchy = build_full_breadcrumb_path(page_hierarchy)


