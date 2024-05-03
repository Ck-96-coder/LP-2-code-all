class HospitalExpertSystem:
    def __init__(self):
        # Initialize hospitals and their details
        self.hospitals = {
            "Hospital A": {"Location": "City A", "Specialty": ["Cardiology", "Orthopedics"], "Rating": 4.5},
            "Hospital B": {"Location": "City B", "Specialty": ["Neurology", "Oncology"], "Rating": 4.8},
            "Hospital C": {"Location": "City C", "Specialty": ["Pediatrics", "Dermatology"], "Rating": 4.2},
            # Add more hospitals with their details
        }

    def find_hospital(self, specialty=None, location=None, rating=None):
        # Filter hospitals based on user's requirements
        filtered_hospitals = []
        for hospital, details in self.hospitals.items():
            if (specialty is None or specialty in details["Specialty"]) and \
                    (location is None or location == details["Location"]) and \
                    (rating is None or rating <= details["Rating"]):
                filtered_hospitals.append(hospital)
        return filtered_hospitals

# Function to get user's requirements
def get_user_requirements():
    specialty = input("Enter desired specialty (Leave blank if not specific): ").strip()
    location = input("Enter desired location (Leave blank if not specific): ").strip()
    rating = float(input("Enter desired minimum rating (Leave blank if not specific): ") or 0)
    return specialty, location, rating

# Main function to interact with the expert system
def main():
    expert_system = HospitalExpertSystem()
    specialty, location, rating = get_user_requirements()
    recommended_hospitals = expert_system.find_hospital(specialty, location, rating)
    if recommended_hospitals:
        print("Recommended Hospitals:")
        for hospital in recommended_hospitals:
            print("-", hospital)
    else:
        print("No hospitals match the specified criteria.")

# Run the main function
if __name__ == "__main__":
    main()


# Enter desired specialty (Leave blank if not specific): Pediatrics
# Enter desired location (Leave blank if not specific): 
# Enter desired minimum rating (Leave blank if not specific): 4.0
# Recommended Hospitals:
# - Hospital C

# Enter desired specialty (Leave blank if not specific): Neurology
# Enter desired location (Leave blank if not specific): City B
# Enter desired minimum rating (Leave blank if not specific): 4.7
# Recommended Hospitals:
# - Hospital B

# Enter desired specialty (Leave blank if not specific): Dermatology
# Enter desired location (Leave blank if not specific): City A
# Enter desired minimum rating (Leave blank if not specific): 
# Recommended Hospitals:
# No hospitals match the specified criteria.

