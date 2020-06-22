from tkinter import *

root = Tk()
root.title("SW Damage Calculator")

frame1 = LabelFrame(root, text="Single Stat Scaling", padx=10, pady=10)
frame1.grid(row=1, column=0)

frame2 = LabelFrame(root, text="Double Stat Scaling", padx=10, pady=10)
frame2.grid(row=1, column=1)


# to add: per buff damage, brand, own hp scaling damage
def scaletype():
    def atkscaling():
        def totalstat():
            b_atk = int(b_atk_entry.get())
            r_atk = int(r_atk_entry.get())
            cd_stat = int(cd_stat_entry.get())
            atoweratk_stat = getdouble(atoweratk_stat_entry.get())
            atowerele_stat = getdouble(atowerele_stat_entry.get())
            atowercd_stat = getdouble(atowercd_stat_entry.get())
            atowerhp_stat = getdouble(atowerhp_stat_entry.get())
            leadskill_stat = int(leadskill_stat_entry.get())
            en_def_stat = int(en_def_stat_entry.get())
            skill_multiplier = int(multiplier_entry.get())
            skill_ups = int(skill_ups_entry.get())
            def_break_toggle = getdouble(def_break_val.get())
            atk_buff_toggle = getdouble(atk_buff_val.get())
            ignore_def_toggle = int(ignore_def_val.get())
            en_hp_stat = int(en_hp_stat_entry.get())
            en_hp_multiplier_stat = int(en_hp_multiplier_stat_entry.get())
            ex_boss_dmg_stat = int(ex_boss_dmg_multiplier.get())
            self_rhp_stat = int(self_rhp_stat_entry.get())
            self_bhp_stat = int(self_bhp_stat_entry.get())
            self_hp_multiplier_stat = int(self_hp_multiplier_stat_entry.get())

            tot_dmg.set((
                                (((b_atk + r_atk +
                                   ((atoweratk_stat / 100) * b_atk) +
                                   ((atowerele_stat / 100) * b_atk) +
                                   ((leadskill_stat / 100) * b_atk)) * atk_buff_toggle) + (
                                         en_hp_stat * en_hp_multiplier_stat) + (
                                         (self_rhp_stat + atowerhp_stat * self_bhp_stat) * self_hp_multiplier_stat)) *
                                (1 + ((atowercd_stat + cd_stat + skill_ups) / 100))) *
                        (skill_multiplier / 100) * (1 + (ex_boss_dmg_stat / 100)) *
                        (1000 / (1140 + 3.5 * (en_def_stat * def_break_toggle * ignore_def_toggle))))

        baseatk = Label(frame1, text="Base Attack")
        defaultentry1 = StringVar()
        defaultentry1.set(0)
        b_atk_entry = Entry(frame1, textvariable=defaultentry1)

        runeatk = Label(frame1, text="Bonus Attack from Runes")
        defaultentry2 = StringVar()
        defaultentry2.set(0)
        r_atk_entry = Entry(frame1, text=defaultentry2)

        cdstat = Label(frame1, text="Critical Damage %")
        defaultentry3 = StringVar()
        defaultentry3.set(0)
        cd_stat_entry = Entry(frame1, text=defaultentry3)

        leadskill = Label(frame1, text="Leader Skill %")
        defaultentry4 = StringVar()
        defaultentry4.set(0)
        leadskill_stat_entry = Entry(frame1, text=defaultentry4)

        endefstat = Label(frame1, text="Enemy Defence")
        defaultentry5 = StringVar()
        defaultentry5.set(0)
        en_def_stat_entry = Entry(frame1, text=defaultentry5)

        multiplier = Label(frame1, text="Skill Multiplier")
        defaultentry6 = StringVar()
        defaultentry6.set(0)
        multiplier_entry = Entry(frame1, text=defaultentry6)

        skillups = Label(frame1, text="Damage from Skill Ups")
        defaultentry7 = StringVar()
        defaultentry7.set(0)
        skill_ups_entry = Entry(frame1, text=defaultentry7)

        enemyhpstat = Label(frame1, text="Enemy HP")
        defaultentry8 = StringVar()
        defaultentry8.set(0)
        en_hp_stat_entry = Entry(frame1, text=defaultentry8)

        enemyhpmultiplier = Label(frame1, text="Enemy HP Multiplier %")
        defaultentry9 = StringVar()
        defaultentry9.set(0)
        en_hp_multiplier_stat_entry = Entry(frame1, text=defaultentry9)

        extrabossdmg = Label(frame1, text="Extra Damage to Boss %")
        defaultentry10 = StringVar()
        defaultentry10.set(0)
        ex_boss_dmg_multiplier = Entry(frame1, text=defaultentry10)

        selfhpmultiplier = Label(frame1, text="Self HP Multiplier %")
        defaultentry11 = StringVar()
        defaultentry11.set(0)
        self_hp_multiplier_stat_entry = Entry(frame1, text=defaultentry11)

        selfbhpstat = Label(frame1, text="Self Base HP")
        defaultentry12 = StringVar()
        defaultentry12.set(0)
        self_bhp_stat_entry = Entry(frame1, text=defaultentry12)

        selfrhpstat = Label(frame1, text="Self Rune HP")
        defaultentry13 = StringVar()
        defaultentry13.set(0)
        self_rhp_stat_entry = Entry(frame1, text=defaultentry13)

        atoweratk = Label(frame1, text="Arena Tower Elemental ATK %")
        atoweratk_stat_entry = StringVar(frame1)
        atoweratk_stat_entry.set('0')
        atoweratklvl = OptionMenu(frame1, atoweratk_stat_entry, '0', '3', '5', '7', '9', '11', '13', '15', '17', '19',
                                  '21')

        atowerele = Label(frame1, text="Arena Tower ATK %")
        atowerele_stat_entry = StringVar(frame1)
        atowerele_stat_entry.set('0')
        atowerelelvl = OptionMenu(frame1, atowerele_stat_entry, '0', '2', '4', '6', '8', '10', '12', '14', '16', '18',
                                  '20')

        atowerhp = Label(frame1, text="Arena Tower HP %")
        atowerhp_stat_entry = StringVar(frame1)
        atowerhp_stat_entry.set('0')
        atowerhplvl = OptionMenu(frame1, atowerhp_stat_entry, '0', '2', '4', '6', '8', '10', '12', '14', '16', '18',
                                 '20')

        atowercd = Label(frame1, text="Arena CD Tower %")
        atowercd_stat_entry = StringVar(frame1)
        atowercd_stat_entry.set('0')
        atowercdlvl = OptionMenu(frame1, atowercd_stat_entry, '0', '2', '5', '7', '10', '12', '15', '17', '20', '22',
                                 '25')

        defbreak = Label(frame1, text="Defence Break")
        def_break_val = DoubleVar(frame1)
        def_break = Checkbutton(frame1, offvalue=1, onvalue=0.3, variable=def_break_val)
        def_break_val.set(1)

        atkbuff = Label(frame1, text="Attack Buff")
        atk_buff_val = DoubleVar(frame1)
        atk_buff = Checkbutton(frame1, offvalue=1, onvalue=1.5, variable=atk_buff_val)
        atk_buff_val.set(1)

        ignoredef = Label(frame1, text="Ignore Defence")
        ignore_def_val = DoubleVar(frame1)
        ignore_def = Checkbutton(frame1, offvalue=1, onvalue=0, variable=ignore_def_val)
        ignore_def_val.set(1)

        tot_dmg = IntVar()
        tot_damage = Label(frame1, textvariable=tot_dmg)

        add_stats = Button(frame1, text="Total Stat", command=totalstat)

        baseatk.grid(row=2, column=0)
        b_atk_entry.grid(row=2, column=1)

        runeatk.grid(row=3, column=0)
        r_atk_entry.grid(row=3, column=1)

        cdstat.grid(row=4, column=0)
        cd_stat_entry.grid(row=4, column=1)

        endefstat.grid(row=5, column=0)
        en_def_stat_entry.grid(row=5, column=1)

        multiplier.grid(row=6, column=0)
        multiplier_entry.grid(row=6, column=1)

        skillups.grid(row=7, column=0)
        skill_ups_entry.grid(row=7, column=1)

        leadskill.grid(row=8, column=0)
        leadskill_stat_entry.grid(row=8, column=1)

        extrabossdmg.grid(row=11, column=0)
        ex_boss_dmg_multiplier.grid(row=11, column=1)

        tot_damage.grid(row=20, column=1)
        add_stats.grid(row=21, column=1)

        atoweratk.grid(row=2, column=4)
        atoweratklvl.grid(row=2, column=5)

        atowerele.grid(row=3, column=4)
        atowerelelvl.grid(row=3, column=5)

        atowercd.grid(row=4, column=4)
        atowercdlvl.grid(row=4, column=5)

        atowerhp.grid(row=5, column=4)
        atowerhplvl.grid(row=5, column=5)

        atkbuff.grid(row=6, column=4)
        atk_buff.grid(row=6, column=5)

        defbreak.grid(row=7, column=4)
        def_break.grid(row=7, column=5)

        ignoredef.grid(row=8, column=4)
        ignore_def.grid(row=8, column=5)

        enemyhpmultiplier.grid(row=2, column=2)
        en_hp_multiplier_stat_entry.grid(row=2, column=3)

        enemyhpstat.grid(row=3, column=2)
        en_hp_stat_entry.grid(row=3, column=3)

        selfhpmultiplier.grid(row=4, column=2)
        self_hp_multiplier_stat_entry.grid(row=4, column=3)

        selfbhpstat.grid(row=5, column=2)
        self_bhp_stat_entry.grid(row=5, column=3)

        selfrhpstat.grid(row=6, column=2)
        self_rhp_stat_entry.grid(row=6, column=3)

    def defscaling():
        def totalstat1():
            b_def = int(b_stat_entry.get())
            r_def = int(r_stat_entry.get())
            cd_stat = int(cd_stat_entry.get())
            atowerdef_stat = int(atower1_stat_entry.get())
            atower2_stat = int(atower2_stat_entry.get())
            atowercd_stat = int(atowercd_stat_entry.get())
            leadskill_stat = int(leadskill_stat_entry.get())
            en_def_stat = int(en_def_stat_entry.get())
            skill_multiplier = int(multiplier_entry.get())
            skill_ups = int(skill_ups_entry.get())
            def_break_toggle = getdouble(def_break_val.get())
            atk_buff_toggle = getdouble(atk_buff_val.get())

            tot_dmg.set((
                                ((b_def + r_def +
                                  ((atowerdef_stat / 100) * b_def) +
                                  ((atower2_stat / 100) * b_def) +
                                  ((leadskill_stat / 100) * b_def)) * atk_buff_toggle) *
                                (1 + ((atowercd_stat + cd_stat + skill_ups) / 100))) *
                        (skill_multiplier / 100) *
                        (1000 / (1140 + 3.5 * (en_def_stat * def_break_toggle))))

        basestat = Label(frame1, text="Base Attack")
        b_stat_entry = Entry(frame1)

        runestat = Label(frame1, text="Bonus Attack from Runes")
        r_stat_entry = Entry(frame1)

        cdstat = Label(frame1, text="Critical Damage %")
        cd_stat_entry = Entry(frame1)

        leadskill = Label(frame1, text="Leader Skill %")
        leadskill_stat_entry = Entry(frame1)

        endefstat = Label(frame1, text="Enemy Defence")
        en_def_stat_entry = Entry(frame1)

        multiplier = Label(frame1, text="Skill Multiplier")
        multiplier_entry = Entry(frame1)

        skillups = Label(frame1, text="Damage from Skill Ups")
        skill_ups_entry = Entry(frame1)

        atower1 = Label(frame1, text="Arena Tower Stat 1 %")
        atower1_stat_entry = StringVar(frame1)
        atower1_stat_entry.set('0')
        atower1lvl = OptionMenu(frame1, atower1_stat_entry, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                                '25')

        atower2 = Label(frame1, text="Arena Tower Stat 2 %")
        atower2_stat_entry = StringVar(frame1)
        atower2_stat_entry.set('0')
        atower2lvl = OptionMenu(frame1, atower2_stat_entry, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                                '25')

        atowercd = Label(frame1, text="Arena CD Tower %")
        atowercd_stat_entry = StringVar(frame1)
        atowercd_stat_entry.set('0')
        atowercdlvl = OptionMenu(frame1, atowercd_stat_entry, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                                 '25')

        defbreak = Label(frame1, text="Defence Break")
        def_break_val = DoubleVar(frame1)
        def_break = Checkbutton(frame1, offvalue=1, onvalue=0.3, variable=def_break_val, textvariable=def_break_val)
        def_break_val.set(1)

        atkbuff = Label(frame1, text="Attack Buff")
        atk_buff_val = DoubleVar(frame1)
        atk_buff = Checkbutton(frame1, offvalue=1, onvalue=1.5, variable=atk_buff_val, textvariable=atk_buff_val)
        atk_buff_val.set(1)

        tot_dmg = DoubleVar()
        tot_damage = Label(frame1, textvariable=tot_dmg)

        add_stats = Button(frame1, text="Total Stat", command=totalstat1)

        basestat.grid(row=2, column=0)
        b_stat_entry.grid(row=2, column=1)

        runestat.grid(row=3, column=0)
        r_stat_entry.grid(row=3, column=1)

        cdstat.grid(row=4, column=0)
        cd_stat_entry.grid(row=4, column=1)

        endefstat.grid(row=5, column=0)
        en_def_stat_entry.grid(row=5, column=1)

        multiplier.grid(row=6, column=0)
        multiplier_entry.grid(row=6, column=1)

        skillups.grid(row=7, column=0)
        skill_ups_entry.grid(row=7, column=1)

        leadskill.grid(row=8, column=0)
        leadskill_stat_entry.grid(row=8, column=1)

        tot_damage.grid(row=9, column=1)
        add_stats.grid(row=10, column=1)

        atower1lvl.grid(row=2, column=3)
        atower1.grid(row=2, column=2)

        atower2lvl.grid(row=3, column=3)
        atower2.grid(row=3, column=4)

        atowercdlvl.grid(row=4, column=3)
        atowercd.grid(row=4, column=2)

        atkbuff.grid(row=5, column=2)
        atk_buff.grid(row=5, column=3)

        defbreak.grid(row=6, column=2)
        def_break.grid(row=6, column=3)

    atk_scaling = Button(frame1, text="Attack Scaling", command=atkscaling)
    atk_scaling.grid(row=1, column=0)


ScalingButton1 = Button(frame1, text="Single Stat Scaling", command=scaletype)
ScalingButton1.grid(row=0, column=0)

root.mainloop()
