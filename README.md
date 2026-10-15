<div align="center">

#  Low-Level System Design Case Studies

**Object-oriented design (LLD) solutions for classic machine-coding problems: classes, relationships, design patterns and clean code.**

![Focus](https://img.shields.io/badge/Focus-Low%20Level%20Design-blue)
![Case Studies](https://img.shields.io/badge/Case%20Studies-3-brightgreen)
![Approach](https://img.shields.io/badge/Approach-OOP%20%7C%20SOLID-orange)

</div>

---

##  About

This repository is where I try to **understand and solve Low-Level Design (LLD) case studies**. Where High-Level Design asks "which services and databases do we need?", Low-Level Design asks "how do we model this in code?": which classes, which responsibilities, which relationships, and which design patterns keep it easy to extend.

Each folder contains one problem and my solution. It is part of my preparation toward a senior backend developer profile, alongside my [High-Level System Design Case Studies](https://github.com/SyedaNaziaGit/High-Level-System-Design-Case-Studies).

---

##  Case Studies

| # | Case Study | The problem | Folder |
| :-: | --- | --- | --- |
| 1 |  **ATM Simulation** | Model an ATM: card authentication, balance enquiry, cash withdrawal and deposit, and machine states | [`Design_atm_simulation_lld`](./Design_atm_simulation_lld) |
| 2 |  **Ride Sharing App (Uber)** | Model riders, drivers, ride requests, matching, trip lifecycle and fares | [`Ride_sharing_app_Uber`](./Ride_sharing_app_Uber) |
| 3 |  **Parking Lot System** | Model parking floors, spots, vehicles, tickets, entry/exit and payment | [`parking_lot_system_lld`](./parking_lot_system_lld) |

---

##  My Approach

Every case study follows the same steps:

1. **Clarify requirements**: what is in scope and what is not
2. **Identify entities**: the nouns that become classes
3. **Define responsibilities**: the verbs that become methods
4. **Draw relationships**: inheritance, composition, association
5. **Apply design principles and patterns**: where they genuinely help
6. **Write the code**: clean, extensible and easy to test
7. **Walk through scenarios**: happy paths and edge cases

>  Adjust these steps to match how you actually worked through each problem.

---

##  Concepts Practised

| Concept | Where it helps |
| --- | --- |
| **SOLID principles** | Keeping classes focused and easy to extend |
| **Encapsulation and abstraction** | Hiding internals behind clear interfaces |
| **Inheritance vs composition** | Modelling vehicles, accounts, users and similar entities |
| **State pattern** | ATM machine states (idle, card inserted, authenticated and so on) |
| **Strategy pattern** | Swappable rules such as pricing, fare calculation or driver matching |
| **Factory pattern** | Creating different vehicle types or ride types cleanly |
| **Concurrency basics** | Two users grabbing the same spot or ride at once |

>  These are the patterns that typically fit these three problems. Keep only the ones you actually used.

---

##  Repository Structure

```
Low-Level-System-Design-Case-Studies/
├── Design_atm_simulation_lld/   # ATM simulation
├── Ride_sharing_app_Uber/       # Ride sharing (Uber-style) design
├── parking_lot_system_lld/      # Parking lot system
└── README.md                    # You are here
```

---

##  Running the Code

Open the folder of the case study you want and follow its instructions. A typical run looks like this:

```bash
git clone https://github.com/SyedaNaziaGit/Low-Level-System-Design-Case-Studies.git
cd Low-Level-System-Design-Case-Studies/parking_lot_system_lld
# run the main file of that case study, for example:
python main.py
```

>  Replace `python main.py` with the real entry point and language for each folder.

---

##  Related Repositories

- [High-Level System Design Case Studies](https://github.com/SyedaNaziaGit/High-Level-System-Design-Case-Studies): the HLD counterpart (Cab Booking, Dropbox, URL Shortener, WhatsApp)

- GitHub: [@SyedaNaziaGit](https://github.com/SyedaNaziaGit)

⭐ If this helped you prepare for LLD interviews, consider giving it a star!
