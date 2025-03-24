# 🧟 Zombie Spread Simulation

This program analyzes a dataset of zombie spread interactions and categorizes people based on their contact behavior. It simulates how a zombie virus might spread in a population using sets, hashmaps, and recursive logic to model contact chains, virality, and more.

---

## 📌 Features

- **Efficient Contact Tracing:**  
  Uses sets and dictionaries for fast insertion and lookup (average case O(1)).

- **Categorization:**
  - **Patient Zeros:** Spreaders who were never contacted by anyone.
  - **Potential Zombies:** People contacted by spreaders but are not spreaders themselves.
  - **Regular Zombies:** People who had contact with both spreaders and potential zombies.
  - **Spreader Zombies:** People who only contacted potential zombies.
  - **Zombie Predators:** People who only contacted other spreaders.

- **Virality & Contact Metrics:**
  - Computes and prints most viral individuals.
  - Identifies most contacted individuals.

- **Maximum Distance Calculation:**  
  Recursively determines how many contact steps each person is from a potential zombie.

---

## 🧑‍💻 Data Input

- The dataset must be a plain text file where each line represents one spreader's contacts.

**Format:**

```
SPREADER,CONTACT1,CONTACT2,...
```

**Example:**

```
CHRIS,JANE,MIKE
MIKE,JOHN
ALEX,CHRIS
```

The program reads from a file named:  
```plaintext
zombie-input/Dataset3.txt
```

> 📁 Make sure this file and path exist when you run the program.

---

## 📂 Output

- Results are written to a file called `output.txt`.
- It includes:
  - Sorted contact records.
  - Lists of patient zeros, potential zombies, and others.
  - Most viral and most contacted people.
  - Maximum distance from potential zombies.
  - Extra info: spreader zombies, regular zombies, and zombie predators.

---

## ⚙️ Performance Notes

- **Sorting:** Python’s built-in Timsort (O(n log n)) is used for sorted outputs.
- **Set/Dict Operations:** Average time complexity of O(1) for lookups and insertions.

---

## 🚀 Running the Program

Ensure you have Python 3 installed and then simply run:

```bash
python zombie_simulation.py
```

The output will be generated in `output.txt`.

---

## 🧠 Concepts Practiced

- Hashing and dictionary operations.
- Recursion for graph traversal.
- Simulation of network spread behavior.
- Categorization using logical constraints.

---

## ✍️ Author

Endi Troqe
