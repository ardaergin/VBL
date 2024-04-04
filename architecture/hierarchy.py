page_hierarchy = {
    "home": 0,

    "how-to-participate": {
        "parent": "home", 
        "display": "How to Participate"
        },
    
    "overview-on-conducting-a-study": {
        "parent": "home", 
        "display": "Overview on Conducting a Study"
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
                "preparation": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Preparation"
                    },
                "ethical-approval": {
                    "parent": "fill-in-the-study-information", 
                    "display": "Ethical Approval"
                    },

        "initial-study-verification": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Initial Study Verification"
            },

        "schedule-a-pilot-testing": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Schedule a Pilot Testing"
            },
        
        "pick-available-dates": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Pick Available Dates"
            },

        "arranging-time-slots": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Arranging Time Slots"
            },
        
        "arranging-time-slots": {
            "parent": "overview-on-conducting-a-study", 
            "display": "Arranging Time Slots"
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


