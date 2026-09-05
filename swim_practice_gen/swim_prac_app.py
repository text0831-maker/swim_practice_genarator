#Swimming practice generator
import webbrowser
import random
import streamlit as st

#Customazation
time = st.selectbox(
    "How long should your practice be? (hours)",
    ['0.5', '1', '1.5', '2', '2+'])
if time == '2+':
    time = 2

time = float(time)

stroke = st.selectbox(
    "What do you want to work on?",
    ["Free", "Fly", "Breast", "Back", "IM"])

stroke_id = ["Free", "Fly", "Breast", "Back", "IM"].index(stroke)

focus = st.radio(
    "Would you like a special focus?",
    ["None", "Sprint", "Distance"]
)

if focus == "Sprint":
    focus = "s"
elif focus == "Distance":
    focus = "d"
else:
    focus = "n"

if st.button("Generate Practice"):
    #Warmup is always a 500fr
    st.header("Warmup")
    st.write("500 Free")
    
    
    #Drills
    
    #Drill lists
    
    free_drills = ["8x50 Catch-Up Drill", "8x50 Fingertip Drag", "8x50 6-Kick Switch", "8x25 Head-Lead Balance", "8x25 Single-Arm Free", "8x50 Fist Swim", "8x25 Tarzan Swim", "4x100 Pull with Buoy", "8x25 Breathing Every 3", "8x50 Descend Stroke Count"]
    
    fly_drills = ["8x25 Body Dolphin", "8x25 Single-Arm Fly", "8x25 3-3-3 Drill", "8x25 Right Arm Fly", "8x25 Left Arm Fly", "8x25 Fly with 2 Kicks per Pull", "6x50 Fly Kick on Back", "8x25 Butterfly with Fins", "8x25 Breathing Every Other Stroke", "4x50 Fly Drill/Swim"]
    
    breast_drills = ["8x25 2-Kick 1-Pull", "8x25 Breast Kick on Back", "8x25 Glide Focus", "8x25 Breast Timing Drill", "8x25 Pullout Practice", "8x25 Fast Recovery Drill", "8x25 Narrow Kick Drill", "4x50 Breast Drill/Swim", "8x25 Stroke Count Focus", "8x25 Kick-Pull Separation"]
    
    back_drills = ["8x25 6-Kick Switch", "8x25 Single-Arm Back", "8x25 Rotation Drill", "8x25 Head-Still Drill", "6x50 Back Kick", "8x25 Double-Arm Back", "8x25 Catch-Up Back", "8x25 Underwater Dolphin to Breakout", "4x50 Back Drill/Swim", "8x25 Stroke Count Focus"]
    
    im_sprint_drills = ["4x(25 Fly Sprint, 25 Easy)", "4x(25 Back Sprint, 25 Easy)", "4x(25 Breast Sprint, 25 Easy)", "4x(25 Free Sprint, 25 Easy)", "8x25 Stroke Order Sprint"]
    
    im_distance_drills = ["8x50 IM Order Drill", "4x100 IM Kick", "8x75 Stroke Drill", "4x200 IM Drill"]
    
    im_drills = ["8x50 IM Order Drill", "4x100 IM Drill", "8x25 Transition Practice", "8x25 Underwater Focus", "4x75 Stroke Drill", "8x25 Fly-to-Back Turns", "8x25 Back-to-Breast Turns", "8x25 Breast-to-Free Turns", "4x100 IM Kick", "8x25 Stroke Technique Choice"]
    
    sprint_drills = ["8x25 Fast Breakouts", "8x25 Underwater Dolphins", "8x25 Race Finish Practice", "8x25 Dive and Breakout", "8x25 Explosive Push-Offs", "8x25 Sprint Kick", "8x25 High Tempo Swimming", "6x50 Build to Sprint", "8x25 Stroke Count Sprint", "8x25 Reaction Starts"]
    
    distance_drills = ["8x50 Long Stroke Count", "4x100 Pull", "8x25 Breathing Pattern","8x50 Descend", "4x75 Technique Focus", "8x50 Negative Split", "8x50 Smooth Tempo", "4x100 Kick", "8x25 Efficiency Focus", "4x200 Pull with Paddles"]
    
    
    drill_list = [free_drills, fly_drills, breast_drills, back_drills, im_drills]
    
    #Randomly selects some drills depending on the cusomazation
    selected_drills = random.sample(drill_list[stroke_id], round(time*2.5))


    #Main set
    
    #Sets list

    free_main = ["10x100 Free Descend 1-5, 6-10", "20x50 Free Race Tempo", "5x200 Free Negative Split", "3x400 Free Aerobic", "16x25 Free Sprint", "8x75 Free Build", "6x150 Free Threshold", "4x300 Free Steady", "12x50 Free Descend", "4x100 Free Race Pace"]
    
    fly_main = ["12x25 Fly Build to Sprint", "8x50 Fly Drill/Swim", "6x75 Fly Strong", "4x100 Fly on Rest", "16x25 Fly Race Pace", "8x25 Fly Fast", "5x100 Fly Descend", "10x50 Fly Moderate", "4x75 Fly Sprint", "20x25 Fly Technique"]
    
    breast_main = ["12x50 Breast Stroke Count Focus", "8x100 Breast Descend", "16x25 Breast Sprint", "6x75 Breast Race Pace", "4x200 Breast Aerobic", "10x50 Breast Build", "5x100 Breast Strong", "12x25 Breast Pullout Focus", "8x50 Breast Fast", "4x150 Breast Threshold"]
    
    back_main = ["10x100 Back Descend", "12x50 Back Race Tempo", "8x75 Back Strong", "20x25 Back Sprint", "4x200 Back Aerobic", "6x150 Back Threshold", "10x50 Back Build", "8x100 Back Pace", "16x25 Back Fast", "4x300 Back Steady"]
    
    im_main = ["8x100 IM", "4x200 IM", "16x25 Stroke Order Sprint", "6x150 IM", "3x300 IM Aerobic", "8x50 IM Fast", "5x200 IM Descend", "12x25 Stroke Order Sprint", "4x100 IM Race Pace", "10x75 IM Strong"]
    
    im_sprint_main = ["16x25 IM Order Sprint", "8x50 IM Race Pace", "4x100 IM Broken Race Pace"]
    
    im_distance_main = ["8x100 IM", "5x200 IM Descend", "3x400 IM", "10x75 IM Strong"]
    
    sprint_main = ["24x25 All-Out Sprint", "12x50 Sprint from Push", "8x25 Sprint from Blocks", "16x25 Race Pace", "4 Rounds: 50 Sprint + 100 Easy", "20x25 Max Speed", "12x25 Dive Sprints", "8x50 Broken 100 Pace", "16x15m Breakout Sprint", "6x50 Fast with Full Recovery"]
    
    distance_main = ["3x500 Free Aerobic", "10x200 Free Steady", "5x400 Free Negative Split", "1x1650 Free", "4x800 Free Aerobic", "20x100 Free Threshold", "8x300 Free Steady", "15x200 Pull", "6x500 Free Build", "30x50 Free Aerobic"]
    
    
    main_list = [free_main, fly_main, breast_main, back_main, im_main]
    
    #Randomly selects some main set workouts depending on the cusomazation
    selected_mains = random.sample(main_list[stroke_id], max(1, round(time * 2)))

    #Changes set depending on if it's a sprint, distance, or none set and chooses different ones for IM
    if focus == "s":
        if stroke_id == 4:      # IM
            available = list(set(im_sprint_drills) - set(selected_drills))
            if available:
                selected_drills += random.sample(available, 1)
            available = list(set(im_sprint_main) - set(selected_mains))
            if available:
                selected_mains += random.sample(available, 1)
    else:
        available = list(set(sprint_drills) - set(selected_drills))
        if available:
            selected_drills += random.sample(available, 1)
        available = list(set(sprint_main) - set(selected_mains))
        if available:
            selected_mains += random.sample(available, 1)

    if focus == "d":
        if stroke_id == 4:
            available = list(set(im_distance_drills) - set(selected_drills))
            if available:
                selected_drills += random.sample(available, 1)
            available = list(set(im_distance_main) - set(selected_mains))
            if available:
                selected_mains += random.sample(available, 1)
    else:
        available = list(set(distance_drills) - set(selected_drills))
        if available:
            selected_drills += random.sample(available, 1)
        available = list(set(distance_main) - set(selected_mains))
        if available:
            selected_mains += random.sample(available, 1)
    
    #Prints out drills and main set
    
    st.header("Drills")
    
    for drill in selected_drills:
        st.write(f"• {drill}")
        
    st.header("Main Set (Repeat this section twice)")

    for main in selected_mains:
        st.write(f"• {main}")

    #Cooldown is always a 500fr
    st.header("Cooldown")
    st.write("500 Free")

    #Drill Help
    st.header("Drill Help")

    with open("Swim Drill Guide.pdf", "rb") as file:
        pdf = file.read()

    st.download_button(
        label="Open Drill Guide",
        data=pdf,
        file_name="Swim Drill Guide.pdf",
        mime="application/pdf"
    )
