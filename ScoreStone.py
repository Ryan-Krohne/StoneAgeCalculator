from tkinter import Tk, Button, Label, simpledialog

# Initialize counters and window

pointsFromHuts = total = tools = toolMultiplier = people = peopleM = farms = farmMultiplier = culture = minCulture = maxCulture = huts = hutMultiplier = 0

#again...
window = Tk()
window.title("Counter Overlay")

# Set window attributes for on-top overlay with no border or title bar
window.overrideredirect(True)
window.attributes('-topmost', True)
window.attributes('-fullscreen', False)  # Remove for non-fullscreen window

# Function to update the animal total label


def update_totals():
    global minCulture, maxCulture, pointsFromHuts
    tool_points = tools * toolMultiplier
    tool_total_label.config(text=f"Tools: {tool_points} points")
    people_points = people * peopleM
    people_total_label.config(text=f"People: {people_points} points")
    farm_points = farms * farmMultiplier
    farm_total_label.config(text=f"Farm: {farm_points} points")
    hut_points = huts * hutMultiplier
    hut_total_label.config(text=f"Huts: {hut_points} points")

    overallTotal = (tool_points + people_points +
                    farm_points + hut_points+pointsFromHuts)
    minTotal = overallTotal + minCulture
    maxTotal = overallTotal + maxCulture
    overall_total_label.config(
        text=f"Min Score: {minTotal} Max Score: {maxTotal}")


def determine_culture():
    global culture, minCulture, maxCulture
    if culture <= 8:
        maxCulture = culture*culture
        x = (culture//2)
        y = culture-x
        minCulture = (x*x) + (y*y)
    else:
        x = culture-8
        maxCulture = 64+(x*x)
        y = culture//2
        z = culture-y
        minCulture = (y*y)+(z*z)
    culture_total_label.config(text=f"Min: {minCulture}  Max: {maxCulture}")


def add_hut():
    global huts, pointsFromHuts
    try:
        hut_cost = simpledialog.askinteger(
            "Hut Cost", "Enter the number of points the hut costs:")
        if hut_cost is not None and hut_cost >= 0:
            pointsFromHuts += hut_cost
            update_counter("huts", 1)  # Update the hut label
    except ValueError:
        pass


# Create label for tool counter
tool_label = Label(window, text=f"Tools: {tools}", font=("Arial", 15))
tool_label.grid(row=0, column=1, padx=5, pady=5)

# Create buttons for tool counter
tool_plus_button = Button(
    window, text="+", command=lambda: update_counter("tools", 1))
tool_plus_button.grid(row=0, column=2, padx=5, pady=5)

tool_minus_button = Button(
    window, text="-", command=lambda: update_counter("tools", -1))
tool_minus_button.grid(row=0, column=0, padx=5, pady=5)

# Create label for tool multiplier
toolMultiplier_label = Label(window, text=f"Multiplier: {
                             toolMultiplier}", font=("Arial", 15))
toolMultiplier_label.grid(row=1, column=1, padx=5, pady=5)

# Create buttons for tool multiplier
toolMultiplier_plus_button = Button(
    window, text="+", command=lambda: update_counter("toolMultiplier", 1))
toolMultiplier_plus_button.grid(row=1, column=2, padx=5, pady=5)

toolMultiplier_minus_button = Button(
    window, text="-", command=lambda: update_counter("toolMultiplier", -1))
toolMultiplier_minus_button.grid(row=1, column=0, padx=5, pady=5)

# Create label for tool total
tool_total_label = Label(window, text=f"Total Tools: 0", font=("Arial", 15))
tool_total_label.grid(row=2, column=1, padx=5, pady=5)


# Create label for people total
people_total_label = Label(window, text=f"Total People: 0", font=("Arial", 15))
people_total_label.grid(row=5, column=1, padx=5, pady=5)

# Create label for people counter
people_label = Label(window, text=f"People: {people}", font=("Arial", 15))
people_label.grid(row=3, column=1, padx=5, pady=5)

# Create buttons for people counter
people_plus_button = Button(
    window, text="+", command=lambda: update_counter("people", 1))
people_plus_button.grid(row=3, column=2, padx=5, pady=5)

people_minus_button = Button(
    window, text="-", command=lambda: update_counter("people", -1))
people_minus_button.grid(row=3, column=0, padx=5, pady=5)

# Create label for peopleM counter
peopleM_label = Label(window, text=f"Multiplier: {
                      peopleM}", font=("Arial", 15))
peopleM_label.grid(row=4, column=1, padx=5, pady=5)

# Create buttons for peopleM counter
peopleM_plus_button = Button(
    window, text="+", command=lambda: update_counter("peopleM", 1))
peopleM_plus_button.grid(row=4, column=2, padx=5, pady=5)

peopleM_minus_button = Button(
    window, text="-", command=lambda: update_counter("peopleM", -1))
peopleM_minus_button.grid(row=4, column=0, padx=5, pady=5)


# Create label for farm counter
farms_label = Label(window, text=f"Farms: {farms}", font=("Arial", 15))
farms_label.grid(row=6, column=1, padx=5, pady=5)


# Create buttons for farm counter
farm_plus_button = Button(
    window, text="+", command=lambda: update_counter("farms", 1))
farm_plus_button.grid(row=6, column=2, padx=5, pady=5)

farm_minus_button = Button(
    window, text="-", command=lambda: update_counter("farms", -1))
farm_minus_button.grid(row=6, column=0, padx=5, pady=5)

# Create label for farm multiplier
farmMultiplier_label = Label(window, text=f"Multiplier: {
                             farmMultiplier}", font=("Arial", 15))
farmMultiplier_label.grid(row=7, column=1, padx=5, pady=5)

# Create buttons for farm multiplier
farmMultiplier_plus_button = Button(
    window, text="+", command=lambda: update_counter("farmsM", 1))
farmMultiplier_plus_button.grid(row=7, column=2, padx=5, pady=5)

farmMultiplier_minus_button = Button(
    window, text="-", command=lambda: update_counter("farmsM", -1))
farmMultiplier_minus_button.grid(row=7, column=0, padx=5, pady=5)

# Create label for farm total
farm_total_label = Label(window, text=f"Total Farms: 0", font=("Arial", 15))
farm_total_label.grid(row=8, column=1, padx=5, pady=5)


# Create label for culture counter
culture_label = Label(window, text=f"Culture: {culture}", font=("Arial", 15))
culture_label.grid(row=9, column=1, padx=5, pady=5)


# Create buttons for culture counter
culture_plus_button = Button(
    window, text="+", command=lambda: update_counter("culture", 1))
culture_plus_button.grid(row=9, column=2, padx=5, pady=5)

culture_minus_button = Button(
    window, text="-", command=lambda: update_counter("culture", -1))
culture_minus_button.grid(row=9, column=0, padx=5, pady=5)

# Create label for culture total
culture_total_label = Label(
    window, text=f"Total Culture: 0", font=("Arial", 15))
culture_total_label.grid(row=10, column=1, padx=5, pady=5)


# Create label for hut counter
hut_label = Label(window, text=f"Huts: {huts}", font=("Arial", 15))
hut_label.grid(row=11, column=1, padx=5, pady=5)

# Create buttons for hut counter
hut_plus_button = Button(window, text="+", command=add_hut)
hut_plus_button.grid(row=11, column=2, padx=5, pady=5)

hut_minus_button = Button(
    window, text="-", command=lambda: update_counter("huts", -1))
hut_minus_button.grid(row=11, column=0, padx=5, pady=5)

# Create label for hut multiplier
hutMultiplier_label = Label(window, text=f"Multiplier: {
                            hutMultiplier}", font=("Arial", 15))
hutMultiplier_label.grid(row=12, column=1, padx=5, pady=5)

# Create buttons for hut multiplier
hutMultiplier_plus_button = Button(
    window, text="+", command=lambda: update_counter("hutMultiplier", 1))
hutMultiplier_plus_button.grid(row=12, column=2, padx=5, pady=5)

hutMultiplier_minus_button = Button(
    window, text="-", command=lambda: update_counter("hutMultiplier", -1))
hutMultiplier_minus_button.grid(row=12, column=0, padx=5, pady=5)

# Create label for hut total
hut_total_label = Label(window, text=f"Total Huts: 0", font=("Arial", 15))
hut_total_label.grid(row=13, column=1, padx=5, pady=5)


# Create label for overall total
overall_total_label = Label(
    window, text=f"Min Score: 0 Max Score: 0", font=("Arial", 15))
overall_total_label.grid(row=100, column=1, padx=5, pady=5)


# Function to update counters
def update_counter(counter_name, value):
    global tools, toolMultiplier, people, peopleM, farms, farmMultiplier, culture, huts, hutMultiplier
    if counter_name == "tools":
        tools += value
        tools = max(tools, 0)  # Ensure tools counter is not negative
        tool_label.config(text=f"Tools: {tools}")
    elif counter_name == "toolMultiplier":
        toolMultiplier += value
        # Ensure toolMultiplier counter is not negative
        toolMultiplier = max(toolMultiplier, 0)
        toolMultiplier_label.config(text=f"Multiplier: {toolMultiplier}")
    elif counter_name == "people":
        people += value
        people = max(people, 0)  # Ensure people counter is not negative
        people_label.config(text=f"People: {people}")
    elif counter_name == "peopleM":
        peopleM += value
        peopleM = max(peopleM, 0)  # Ensure peopleM counter is not negative
        peopleM_label.config(text=f"Multiplier: {peopleM}")
    elif counter_name == "farms":
        farms += value
        farms = max(farms, 0)  # Ensure peopleM counter is not negative
        farms_label.config(text=f"Farms: {farms}")
    elif counter_name == "farmsM":
        farmMultiplier += value
        # Ensure farmMultiplier counter is not negative
        farmMultiplier = max(farmMultiplier, 0)
        farmMultiplier_label.config(text=f"Multiplier: {farmMultiplier}")
    elif counter_name == "culture":
        culture += value
        culture = min(culture, 16)  # make sure can't go above 16
        culture = max(culture, 0)  # Ensure culture counter is not negative
        culture_label.config(text=f"Culture: {culture}")
        determine_culture()
    elif counter_name == "huts":
        huts += value
        huts = max(huts, 0)  # Ensure huts counter is not negative
        hut_label.config(text=f"Huts: {huts}")
    elif counter_name == "hutMultiplier":
        hutMultiplier += value
        # Ensure hutMultiplier counter is not negative
        hutMultiplier = max(hutMultiplier, 0)
        hutMultiplier_label.config(text=f"Multiplier: {hutMultiplier}")

    update_totals()


# Run the main event loop
window.mainloop()
