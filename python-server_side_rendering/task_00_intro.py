import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if template.strip() == "":
        print("Error: Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate over each attendee
    for i, person in enumerate(attendees, start=1):
        # Replace placeholders with values or 'N/A' if missing
        invitation = template
        for field in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(field)
            value_str = value if value else "N/A"
            invitation = invitation.replace("{" + field + "}", value_str)

        # Write the invitation to an output file
        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
