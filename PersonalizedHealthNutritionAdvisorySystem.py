import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

def get_nutritional_advice(age, gender, goals, height, weight):
    bmi = calculate_bmi(weight, height)
    advice = ""
    weight_status = ""

    if bmi < 18.5:
        weight_status = "Underweight"
        advice = "You are underweight. You should focus on gaining weight in a healthy way.\n\n"
        advice += "Foods to include:\n"
        advice += "- Whole grains (e.g., quinoa, brown rice, oats)\n"
        advice += "- Lean proteins (e.g., chicken, fish, tofu)\n"
        advice += "- Healthy fats (e.g., avocados, nuts, olive oil)\n"
        advice += "- Dairy or dairy alternatives (e.g., milk, yogurt, cheese)\n"
        advice += "- Nutrient-dense fruits and vegetables\n"
    elif bmi >= 18.5 and bmi < 25:
        weight_status = "Normal weight"
        advice = "You have a healthy weight. Maintain a balanced diet and exercise regularly.\n\n"
        advice += "Foods to include:\n"
        advice += "- Whole grains (e.g., quinoa, brown rice, whole wheat bread)\n"
        advice += "- Lean proteins (e.g., chicken, fish, beans)\n"
        advice += "- Healthy fats (e.g., avocado, nuts, seeds)\n"
        advice += "- Dairy or dairy alternatives (e.g., milk, yogurt, tofu)\n"
        advice += "- Colorful fruits and vegetables\n"
    elif bmi >= 25 and bmi < 30:
        weight_status = "Overweight"
        advice = "You are overweight. Focus on reducing your weight through a balanced diet and regular exercise.\n\n"
        advice += "Foods to include:\n"
        advice += "- Whole grains (e.g., quinoa, brown rice, whole wheat pasta)\n"
        advice += "- Lean proteins (e.g., chicken, fish, legumes)\n"
        advice += "- Healthy fats in moderation (e.g., avocado, nuts, olive oil)\n"
        advice += "- Low-fat dairy or dairy alternatives (e.g., skim milk, low-fat yogurt)\n"
        advice += "- Plenty of fruits and vegetables\n"
        advice += "\nFoods to limit or avoid:\n"
        advice += "- Processed foods high in added sugars and unhealthy fats\n"
        advice += "- Sugary beverages\n"
    else:
        weight_status = "Obese"
        advice = "You are obese. Focus on losing weight through a balanced diet and regular exercise.\n\n"
        advice += "Foods to include:\n"
        advice += "- Whole grains (e.g., quinoa, brown rice, whole wheat bread)\n"
        advice += "- Lean proteins (e.g., chicken, fish, legumes)\n"
        advice += "- Healthy fats in moderation (e.g., avocado, nuts, olive oil)\n"
        advice += "- Low-fat dairy or dairy alternatives (e.g., skim milk, low-fat yogurt)\n"
        advice += "- Plenty of fruits and vegetables\n"
        advice += "\nFoods to limit or avoid:\n"
        advice += "- Processed foods high in added sugars and unhealthy fats\n"
        advice += "- Sugary beverages\n"

    if "Diabetic" in goals:
        advice += "\nFor Diabetics:\n"
        advice += "- Focus on consuming complex carbohydrates (e.g., whole grains, legumes)\n"
        advice += "- Choose low glycemic index foods\n"
        advice += "- Limit added sugars and sugary beverages\n"
        advice += "- Include lean proteins\n"
        advice += "- Incorporate healthy fats in moderation\n"
        advice += "- Eat small, frequent meals\n"

    if "Bodybuilder" in goals:
        advice += "\nFor Bodybuilders:\n"
        advice += "- Consume adequate protein to support muscle growth and repair\n"
        advice += "- Include complex carbohydrates for energy\n"
        advice += "- Incorporate healthy fats for overall health\n"
        advice += "- Stay hydrated\n"
        advice += "- Eat balanced meals and snacks throughout the day\n"

    if "Expectant Mother" in goals:
        if gender == "Female":
            advice += "\nFor Expectant Mothers:\n"
            advice += "- Consume a variety of fruits, vegetables, whole grains, and lean proteins\n"
            advice += "- Ensure adequate intake of folate, iron, calcium, and omega-3 fatty acids\n"
            advice += "- Stay hydrated\n"
            advice += "- Limit caffeine and avoid alcohol\n"
            advice += "- Consult with a healthcare professional for specific dietary needs\n"
        else:
            advice += "\nExpectant Mother goal is not applicable for males.\n"

    return weight_status, advice

def show_nutritional_advice():
    age = int(age_entry.get())
    gender = gender_var.get()
    goals = []
    if diabetic_checkbutton_var.get():
        goals.append("Diabetic")
    if bodybuilder_checkbutton_var.get():
        goals.append("Bodybuilder")
    if expectant_mother_checkbutton_var.get() and gender == "Female":
        goals.append("Expectant Mother")
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    weight_status, advice = get_nutritional_advice(age, gender, goals, height, weight)
    messagebox.showinfo("Nutritional Advice", "Weight Status: {}\n\n{}".format(weight_status, advice))

def track_progress():
    weight = float(weight_entry.get())
    progress = "Weight: {} kg".format(weight)
    progress_listbox.insert(tk.END, progress)

    if len(progress_listbox.get(0, tk.END)) > 1:
        initial_weight = float(progress_listbox.get(0).split(": ")[-1].split(" kg")[0])
        current_weight = float(progress_listbox.get(tk.END).split(": ")[-1].split(" kg")[0])
        weight_change = current_weight - initial_weight
        if weight_change > 0:
            progress_message = "You have gained {} kg since starting.\n\n".format(abs(weight_change))
            progress_message += "Additional advice for weight gain:\n"
            progress_message += "- Increase caloric intake with nutrient-dense foods\n"
            progress_message += "- Include healthy sources of protein, carbohydrates, and fats\n"
            progress_message += "- Consider incorporating resistance training exercises\n"
        elif weight_change < 0:
            progress_message = "You have lost {} kg since starting.\n\n".format(abs(weight_change))
            progress_message += "Additional advice for weight loss:\n"
            progress_message += "- Continue following the recommended dietary guidelines\n"
            progress_message += "- Monitor portion sizes and avoid excessive calorie intake\n"
            progress_message += "- Incorporate regular cardiovascular and strength training exercises\n"
        else:
            progress_message = "Your weight has remained unchanged since starting.\n\n"
            progress_message += "Continue following the recommended dietary guidelines and exercise regularly."

        messagebox.showinfo("Progress Update", progress_message)

# Create a Tkinter window
window = tk.Tk()
window.title("Nutritional Advice and Progress Tracker")
window.geometry("400x650")

# Change the color of the window
window.configure(bg="cyan")

# Age Label and Entry
age_label = tk.Label(window, text="Age:")
age_label.pack(pady=5)
age_entry = tk.Entry(window)
age_entry.pack(pady=5)

# Gender Label and Radio Buttons
gender_label = tk.Label(window, text="Gender:")
gender_label.pack(pady=5)
gender_var = tk.StringVar(value="Male")
gender_male_radio = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
gender_male_radio.pack(pady=2)
gender_female_radio = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
gender_female_radio.pack(pady=2)

# Height Label and Entry
height_label = tk.Label(window, text="Height (cm):")
height_label.pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack(pady=5)

# Weight Label and Entry
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack(pady=5)

# Goals Label and Checkbuttons
goals_label = tk.Label(window, text="Goals:")
goals_label.pack(pady=5)
diabetic_checkbutton_var = tk.BooleanVar()
diabetic_checkbutton = tk.Checkbutton(window, text="Diabetic", variable=diabetic_checkbutton_var)
diabetic_checkbutton.pack(pady=2)
bodybuilder_checkbutton_var = tk.BooleanVar()
bodybuilder_checkbutton = tk.Checkbutton(window, text="Bodybuilder", variable=bodybuilder_checkbutton_var)
bodybuilder_checkbutton.pack(pady=2)
expectant_mother_checkbutton_var = tk.BooleanVar()
expectant_mother_checkbutton = tk.Checkbutton(window, text="Expectant Mother", variable=expectant_mother_checkbutton_var, state="disabled")
expectant_mother_checkbutton.pack(pady=2)

# Update the state of the Expectant Mother checkbox based on the selected gender
def update_expectant_mother_checkbox():
    if gender_var.get() == "Female":
        expectant_mother_checkbutton.config(state="normal")
    else:
        expectant_mother_checkbutton_var.set(False)
        expectant_mother_checkbutton.config(state="disabled")

gender_var.trace("w", lambda *args: update_expectant_mother_checkbox())

# Button to calculate and show advice
calculate_button = tk.Button(window, text="Calculate", command=show_nutritional_advice)
calculate_button.pack(pady=10)

# Progress Tracker
progress_label = tk.Label(window, text="Progress Tracker:")
progress_label.pack(pady=5)
progress_listbox = tk.Listbox(window, width=40, height=10)
progress_listbox.pack(pady=5)

# Button to track progress
track_button = tk.Button(window, text="Track Progress", command=track_progress)
track_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
