# RoboJam – Facilitator Instructions v1

This document outlines the standard process developed by John and the team. Please feel free to adapt these steps as you see fit to best suit your event.

---

## 📅 Prior to the Day

### Volunteer Coordination
* **Calendar Placeholders:** Ensure you have placeholders booked for volunteers. 
  * *Ratio:* You need **one volunteer per team**.
* **Briefing Session:** Suggest holding a briefing session with volunteers 1–2 days prior to explain the setting and answer questions.
* **Key Reminders for Volunteers:**
  * **No Meetings:** Do not book any meetings; be present for the full day.
  * **Device Policy:** DO NOT take out your mobile phone while in the classroom with the children.
  * **Photo Policy:** DO NOT take any photos. The school can take photos and share them later if mutually agreed.
  
### School Liaison Checklist
Clarify the following details with the school well in advance:
* [ ] **Timings:** Arrival time, end of school day, break times, and lunch times.
* [ ] **Lunch Arrangements:** Is lunch provided by the school, or should volunteers bring/buy their own?
* [ ] **Teacher Supervision:** Confirm a teacher will be present at all times.
* [ ] **DBS Checks:** Confirm if volunteers need DBS checks (usually not required if a teacher is present).
* [ ] **Target Audience:** Confirm students are in **Year 5 or Year 6**. Do not try this with younger children unless you want a very tough day.
* [ ] **Student Headcount:** Suggest a **maximum of 40 students**.
  * *Example setup:* 4 students per group = 10 groups = 10 volunteers.

### Required School Logistics & Equipment
Ensure the school secures the following items before the event:

#### Technology
* [ ] **HDMI Capture Compatibility:** Ensure the school has laptops compatible with the HDMI capture devices. For example, Check the required website [https://nerdzap.com/view/] and ensure it is permitted on their network.  They may prefer to use a "Camera" app instead - the main thing is it can be made full screen so the text is readable with minimal clutter in the way.

#### Kit & Consumables
* [ ] **CamJam 3 Kits:** One per group, plus a few spares.
* [ ] **Batteries:** 4x AAA batteries per group.
* [ ] **Extra Sticky Pads:** Foam sticky pads (ideally 3M ones, like those in the CamJam kit).
* [ ] **Masking Tape:** A few rolls (verify it is safe to use on the school floor).
* [ ] **Balloons:** ~60 balloons (cheaper ones work better as they are more "poppable").
* [ ] **Kebab Skewers:** 1 pack.

#### Craft & Utility Items
* [ ] **Craft Items:** Coloured card, sticky tape, felt pens, pipe cleaners, and glittery items.
* [ ] **Lolly Sticks:** A few packs.
* [ ] **Scissors**.

**Bring from Home:** Along side all the kit needed, bring some sandpaper to sharpen kebab sticks.

---

## 🛠️ On the Day: Setup

Once volunteers arrive, lay out the following items on each team's table:

| Hardware & Electronics | Tools & Utilities | Craft Materials |
| :--- | :--- | :--- |
| • Raspberry Pi (with SD card inside)<br>• CamJam Kit<br>• Powerbank<br>• Chromebook<br>• HDMI Capture Device<br>• Wireless keyboard/mouse controller & dongle<br>• 4x AAA batteries | • Scissors<br>• Extra sticky pads<br>• Masking tape<br>• Rulers (for measuring) | • Lolly sticks<br>• Address labels (for making name tags) |

### Logistics & Housekeeping
* Point out the toilets and where refreshments will be served during breaks.
* **Mobile Phone Ban:** Remind volunteers to keep phones out of sight. Pupil use of mobile phones is banned in all schools in England.
* Instruct volunteers to sit at the desks, ready to blend into their assigned pupil groups.
* **Attention Grabbers:** Ask the school if they have a specific way to get the kids' attention (e.g., a clapping pattern). Alternatively, ask for a noisy device like a football rattle, gong, or horn.

---

## 🤖 Running the Day: Step-by-Step

### Phase 1: Welcome & Robot Build (~1 Hour)
1. **Seating:** Let the teacher decide who sits where using their pre-allocated groups.
2. **Introduction:** Welcome the kids, introduce yourselves as being from **NATWEST**, and explain the purpose of the day.
3. **Icebreaker:** Ask if anyone’s sibling has done this before and what they thought of it.
4. **Name Tags:** Have everyone write their first name on an address label and stick it on themselves.
5. **The Build:** Give the teams 1 hour to build their robot. **Emphasise that strength and stability are key**.
6. **Robot Branding:** Instruct each team to choose a robot name and write it in the space provided in their pack. This name should inspire their robot's decoration theme.
7. **Floor Setup:** While the kids are building, tape out the testing lines on the floor:
   * *Challenge 1:* Two parallel lines approximately 2 metres apart.
   * *Challenge 2:* Set up the maze tape simultaneously if time permits.

> 💡 **Facilitator Build Tips & Safety:**
> * Expect a lot of questions about wiring and cutting chassis holes.
> * **Safety:** Facilitators can use knives/blades to assist, but **never** let the children use excessively sharp tools.
> * **Common Error 1:** Forgetting to connect the red battery wire to the positive (+) terminal and the black wire to the negative (-) terminal.
> * **Common Error 2:** Misaligning the motor controller board on the Pi GPIO port. It must line up perfectly with the leftmost pin (looking at the Pi with the GPIO port at the top). **Check this before powering on the Pi**.

### Phase 2: Coding Briefing (Optional)
Once the majority of teams have moving robots, you can optionally connect a spare Pi to a large screen. Gather the students around to show them how to edit and run the code, highlighting the main areas they need to modify.

### Phase 3: Challenge 1 – Distance Challenge
* **Objective:** Drive the robot exactly to the second line.
* **Process:** Run the code, check that it works, detach the HDMI cable, and place the robot on the first line.
* **Execution:** Press **"1"** on the controller to trigger `runChallenge1()`.
* **Scoring:** Measure the distance from the second line. Teams are scored based on how many centimetres they are over or under the target (the scoreboard calculates absolute values, so direction doesn't matter).
* **Official Runs:** Teams can practice as much as they want. When ready, they must declare an "Official Run." They get **two official attempts**, and we record the best score.
* **Time Management:** Set a firm deadline. Remind them that finishing Challenge 1 early gives them more time for the much harder Challenge 2.

### Phase 4: Challenge 2 – The Maze Challenge
* **Setup:** Create an "entrance", an "exit", and a few obstacles between the two lines. Add "checkpoint" lines along the path to award partial progress points.
* **Execution:** Start in the entrance area and press **"2"** on the controller to run `runChallenge2()`.
* **Rules:** Use directional commands (forward, left, right) to navigate the maze and escape through the exit.
* **Scoring:** 
  * **10 points** per checkpoint crossed.
  * **15 points** for successfully exiting the maze.
  * *Disqualification:* If the robot completely leaves the maze (or touches the exterior lines for higher difficulty), the run ends. They retain any points earned up to that point.
* **Attempts:** Two official runs are permitted.

### Phase 5: Challenge 3 – Aesthetic Design
* **Aesthetic Strategy:** Introduce this challenge early if certain children show less interest in programming and prefer the artistic side.
* **Rule:** Decorate the robot to match its chosen name using the provided materials. **Keep craft items out of sight until this phase begins**, otherwise they will start decorating immediately.
* **Tidy Desk Bonus:** Offer an extra **5 points** to the team with the cleanest workstation when judging begins. This saves cleanup time later and can be judged by the teacher.
* **Judging:** Coordinate a specific time for the Head Teacher or a designated guest to judge the designs. Time permitting, have the teacher ask each team for a brief explanation of their approach, then award points:
  * *1st Place:* 20 points
  * *2nd Place:* 15 points
  * *3rd Place:* 10 points
  * *Honourable Mention:* 5 points

---

## ⚔️ The Grand Finale: Robot Battle

### Arena Setup
While the design judging is wrapping up, construct a battle arena using desks or PE benches laid on their sides. The arena should be at least **3m x 3m** or larger.

### Battle Rules
* **Pre-requisites:** Robots must be fully functional and running.
* **Balloons:** Attach two pre-inflated balloons to the cardboard box chassis of each robot. 
  * *Restriction:* Balloons must be attached directly to the box. Extending them out on long sticks or armor-plating them with masking tape is strictly prohibited. Keep plenty of spare balloons handy to toss into the arena for extra action.
* **Weapons:** Have volunteers use masking tape to attach 2–4 sharpened cocktail sticks to the chassis. Ensure they point horizontally or slightly upward.
* **Safety First:** **From this point on, ONLY ADULTS may touch the robots**.
* **The Match:** 
  1. Whip the crowd into a frenzy: Ask the kids if they had fun and get them to make some noise.
  2. The match lasts for **3 minutes**. Teams are allowed to swap drivers mid-match if they choose.
  3. Start the battle with a unified 10-second countdown.
* **Scoring:** Teams earn **10 points** for each un-popped balloon still attached to their robot when time expires.

---

## 👋 Ending the Day

1. **Stop Action:** Call time, instruct kids to put down their controllers into the arena, and have facilitators check the remaining balloons while a colleague updates the scoreboard.
2. **Awards:** Hold a big reveal for the top 3 teams (expect occasional ties).
3. **Dismissal:** Thank everyone. The teacher will then lead the children out for dismissal.
4. **Pack Down:** Ask volunteers to dismantle the robots to recover the bank-owned gear. Leave the cardboard chassis and the disposable CamJam kit pieces for the school to keep or discard.
5. **Clean up Note:** Facilitators are *not* obligated to clean the classroom floors or surfaces.
6. **Feedback:** Hand out feedback forms if available. They are fun for the kids to fill out and can be collected later via the school.

---

## 🔍 Troubleshooting Guide

| Issue | Root Cause | Resolution |
| :--- | :--- | :--- |
| **Wheels do not move at all** | Power or connection failure. | • Check that the battery pack has working batteries and is switched on.<br>• Check that wires are correctly connected to the +/- terminals and screwed down tightly.<br>• Ensure the controller board is securely and accurately seated on the GPIO port. |
| **Robot spins in circles** | Motor polarity reversed *(By far the most common issue)*. | • Swap the two motor wires on the specific motor that is spinning backwards. |
| **Robot veers / does not drive straight** | Mechanical friction or minor motor variance. | • Check for unstable components or parts rubbing against the cardboard box.<br>• Adjust the individual motor speeds directly within the software code to correct a gentle curve. |
| **Persistent motor issues** | Faulty component. | • Swap out the motor controller board for a known working spare.<br>• For highly troublesome builds, systematically swap components out one by one until the fault is isolated. |
| **Python syntax/runtime error** | Accidental code modification. | • Usually caused by "fat-fingering" keys while moving the keyboard, introducing syntax typos.<br>• Check for improper capitalization, which frequently causes issues. |
