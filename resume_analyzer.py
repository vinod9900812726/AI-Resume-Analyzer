print("=== Basic Resume Analyzer ===")

resume = input("Paste your resume text: ").lower()

skills = [
    "python",
    "java",
    "machine learning",
    "generative ai",
    "sql",
    "html",
    "communication"
]

found = []

for skill in skills:
    if skill in resume:
        found.append(skill)

print("\nSkills Found:")

if found:
    for skill in found:
        print("-", skill)
else:
    print("No matching skills found.")

print("\nTotal Skills Found:", len(found))
print("Analysis completed!")
