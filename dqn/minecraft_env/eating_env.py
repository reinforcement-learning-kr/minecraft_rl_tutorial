from past.utils import old_div
import random
from utils import malmoutils

# Task parameters:
NUM_GOALS = 20
GOAL_TYPE = "apple"
GOAL_REWARD = 100
ARENA_WIDTH = 60
ARENA_BREADTH = 60
MOB_TYPE = "Endermite"  # Change for fun, but note that spawning conditions have to be correct - eg spiders will require darker conditions.


# Agent parameters:
agent_stepsize = 1
agent_search_resolution = 30  # Smaller values make computation faster, which seems to offset any benefit from the higher resolution.
agent_goal_weight = 100
agent_edge_weight = -100
agent_mob_weight = -10
agent_turn_weight = 0  # Negative values to penalise turning, positive to encourage.


def getItemXML():
    ''' Build an XML string that contains some randomly positioned goal items'''
    xml = ""
    for item in range(NUM_GOALS):
        x = str(
            random.randint(old_div(-ARENA_WIDTH, 2), old_div(ARENA_WIDTH, 2)))
        z = str(random.randint(old_div(-ARENA_BREADTH, 2),
                               old_div(ARENA_BREADTH, 2)))
        xml += '''<DrawItem x="''' + x + '''" y="210" z="''' + z + '''" type="''' + GOAL_TYPE + '''"/>'''
    return xml


def getCorner(index, top, left, expand=0, y=206):
    ''' Return part of the XML string that defines the requested corner'''
    x = str(-(expand + old_div(ARENA_WIDTH, 2))) if left else str(
        expand + old_div(ARENA_WIDTH, 2))
    z = str(-(expand + old_div(ARENA_BREADTH, 2))) if top else str(
        expand + old_div(ARENA_BREADTH, 2))
    return 'x' + index + '="' + x + '" y' + index + '="' + str(
        y) + '" z' + index + '="' + z + '"'


def getMissionXML(summary, agent_host):
    ''' Build an XML mission string.'''
    spawn_end_tag = ' type="mob_spawner" variant="' + MOB_TYPE + '"/>'
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <About>
          <Summary>Healthy diet. Eating right and wrong objects</Summary>
        </About>

        <ModSettings>
          <MsPerTick>20</MsPerTick>
          <PrioritiseOffscreenRendering>true</PrioritiseOffscreenRendering>
        </ModSettings>

        <ServerSection>
          <ServerInitialConditions>
                <Time>
                    <StartTime>6000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
                <AllowSpawning>false</AllowSpawning>
          </ServerInitialConditions>
          <ServerHandlers>
            <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1"/>
            <DrawingDecorator>
              <DrawCuboid colour="RED" face="UP" type="carpet" x1="-50" x2="50" y1="226" y2="226" z1="-50" z2="50"/>
              <DrawItem type="egg" x="-41" y="250" z="-46"/>
              <DrawItem type="egg" x="-33" y="250" z="-18"/>
              <DrawItem type="egg" x="2" y="250" z="-19"/>
              <DrawItem type="carrot" x="-28" y="250" z="-44"/>
              <DrawItem type="apple" x="41" y="250" z="30"/>
              <DrawItem type="apple" x="-23" y="250" z="18"/>
              <DrawItem type="potato" x="-28" y="250" z="25"/>
              <DrawItem type="pumpkin_pie" x="-12" y="250" z="3"/>
              <DrawItem type="sugar" x="-9" y="250" z="10"/>
              <DrawItem type="sugar" x="2" y="250" z="46"/>
              <DrawItem type="chicken" x="-3" y="250" z="29"/>
              <DrawItem type="egg" x="33" y="250" z="13"/>
              <DrawItem type="carrot" x="0" y="250" z="-1"/>
              <DrawItem type="cake" x="-26" y="250" z="-14"/>
              <DrawItem type="potato" x="49" y="250" z="-5"/>
              <DrawItem type="potato" x="-48" y="250" z="41"/>
              <DrawItem type="potato" x="-48" y="250" z="-12"/>
              <DrawItem type="potato" x="-7" y="250" z="-42"/>
              <DrawItem type="beef" x="26" y="250" z="9"/>
              <DrawItem type="pumpkin_pie" x="-7" y="250" z="-40"/>
              <DrawItem type="sugar" x="-2" y="250" z="-48"/>
              <DrawItem type="egg" x="7" y="250" z="-27"/>
              <DrawItem type="pumpkin_pie" x="17" y="250" z="38"/>
              <DrawItem type="porkchop" x="-8" y="250" z="-6"/>
              <DrawItem type="egg" x="4" y="250" z="31"/>
              <DrawItem type="chicken" x="-49" y="250" z="-11"/>
              <DrawItem type="pumpkin_pie" x="-1" y="250" z="11"/>
              <DrawItem type="apple" x="-6" y="250" z="-35"/>
              <DrawItem type="fish" x="-38" y="250" z="18"/>
              <DrawItem type="cookie" x="34" y="250" z="5"/>
              <DrawItem type="fish" x="46" y="250" z="-11"/>
              <DrawItem type="fish" x="-21" y="250" z="-29"/>
              <DrawItem type="carrot" x="-10" y="250" z="-47"/>
              <DrawItem type="cake" x="-26" y="250" z="26"/>
              <DrawItem type="pumpkin_pie" x="-25" y="250" z="-13"/>
              <DrawItem type="fish" x="43" y="250" z="2"/>
              <DrawItem type="apple" x="46" y="250" z="47"/>
              <DrawItem type="mutton" x="15" y="250" z="-48"/>
              <DrawItem type="beef" x="46" y="250" z="-1"/>
              <DrawItem type="carrot" x="16" y="250" z="6"/>
              <DrawItem type="mutton" x="-27" y="250" z="26"/>
              <DrawItem type="beef" x="35" y="250" z="-13"/>
              <DrawItem type="chicken" x="44" y="250" z="3"/>
              <DrawItem type="rabbit" x="-44" y="250" z="42"/>
              <DrawItem type="egg" x="43" y="250" z="15"/>
              <DrawItem type="rabbit" x="33" y="250" z="-37"/>
              <DrawItem type="fish" x="-9" y="250" z="-25"/>
              <DrawItem type="melon" x="-45" y="250" z="-21"/>
              <DrawItem type="mutton" x="-13" y="250" z="-40"/>
              <DrawItem type="cookie" x="-7" y="250" z="-31"/>
              <DrawItem type="cookie" x="32" y="250" z="-22"/>
              <DrawItem type="rabbit" x="15" y="250" z="16"/>
              <DrawItem type="mutton" x="-37" y="250" z="26"/>
              <DrawItem type="cookie" x="19" y="250" z="47"/>
              <DrawItem type="beef" x="33" y="250" z="-22"/>
              <DrawItem type="melon" x="19" y="250" z="-25"/>
              <DrawItem type="sugar" x="8" y="250" z="10"/>
              <DrawItem type="egg" x="-41" y="250" z="32"/>
              <DrawItem type="beef" x="49" y="250" z="-18"/>
              <DrawItem type="beef" x="-26" y="250" z="8"/>
              <DrawItem type="porkchop" x="-49" y="250" z="19"/>
              <DrawItem type="beef" x="-34" y="250" z="39"/>
              <DrawItem type="potato" x="-26" y="250" z="-24"/>
              <DrawItem type="melon" x="37" y="250" z="-17"/>
              <DrawItem type="melon" x="-49" y="250" z="-49"/>
              <DrawItem type="potato" x="-45" y="250" z="23"/>
              <DrawItem type="potato" x="40" y="250" z="-18"/>
              <DrawItem type="cake" x="-5" y="250" z="-49"/>
              <DrawItem type="chicken" x="34" y="250" z="-9"/>
              <DrawItem type="sugar" x="-8" y="250" z="44"/>
              <DrawItem type="egg" x="-7" y="250" z="-22"/>
              <DrawItem type="carrot" x="20" y="250" z="36"/>
              <DrawItem type="egg" x="-21" y="250" z="-9"/>
              <DrawItem type="sugar" x="50" y="250" z="22"/>
              <DrawItem type="apple" x="31" y="250" z="-13"/>
              <DrawItem type="mutton" x="-46" y="250" z="-23"/>
              <DrawItem type="cake" x="19" y="250" z="-8"/>
              <DrawItem type="beef" x="29" y="250" z="-43"/>
              <DrawItem type="pumpkin_pie" x="-43" y="250" z="37"/>
              <DrawItem type="chicken" x="-12" y="250" z="45"/>
              <DrawItem type="beef" x="-19" y="250" z="2"/>
              <DrawItem type="egg" x="-32" y="250" z="-13"/>
              <DrawItem type="egg" x="41" y="250" z="13"/>
              <DrawItem type="apple" x="34" y="250" z="-13"/>
              <DrawItem type="carrot" x="25" y="250" z="49"/>
              <DrawItem type="rabbit" x="-10" y="250" z="24"/>
              <DrawItem type="chicken" x="45" y="250" z="-27"/>
              <DrawItem type="egg" x="-22" y="250" z="44"/>
              <DrawItem type="melon" x="44" y="250" z="39"/>
              <DrawItem type="beef" x="48" y="250" z="-8"/>
              <DrawItem type="cake" x="-45" y="250" z="18"/>
              <DrawItem type="fish" x="-27" y="250" z="34"/>
              <DrawItem type="potato" x="24" y="250" z="-18"/>
              <DrawItem type="melon" x="50" y="250" z="43"/>
              <DrawItem type="egg" x="-23" y="250" z="34"/>
              <DrawItem type="carrot" x="-11" y="250" z="27"/>
              <DrawItem type="mutton" x="28" y="250" z="-44"/>
              <DrawItem type="rabbit" x="-47" y="250" z="-29"/>
              <DrawItem type="fish" x="17" y="250" z="-5"/>
              <DrawItem type="porkchop" x="-42" y="250" z="25"/>
              <DrawItem type="sugar" x="26" y="250" z="48"/>
              <DrawItem type="melon" x="44" y="250" z="-26"/>
              <DrawItem type="chicken" x="-14" y="250" z="-33"/>
              <DrawItem type="egg" x="17" y="250" z="7"/>
              <DrawItem type="cookie" x="-36" y="250" z="40"/>
              <DrawItem type="cookie" x="-32" y="250" z="28"/>
              <DrawItem type="rabbit" x="48" y="250" z="-18"/>
              <DrawItem type="porkchop" x="24" y="250" z="-24"/>
              <DrawItem type="melon" x="-13" y="250" z="-17"/>
              <DrawItem type="rabbit" x="-25" y="250" z="38"/>
              <DrawItem type="porkchop" x="18" y="250" z="47"/>
              <DrawItem type="porkchop" x="-47" y="250" z="34"/>
              <DrawItem type="mutton" x="-11" y="250" z="10"/>
              <DrawItem type="potato" x="-17" y="250" z="-38"/>
              <DrawItem type="mutton" x="-42" y="250" z="34"/>
              <DrawItem type="potato" x="-4" y="250" z="-33"/>
              <DrawItem type="mutton" x="-10" y="250" z="39"/>
              <DrawItem type="fish" x="44" y="250" z="-38"/>
              <DrawItem type="apple" x="-11" y="250" z="34"/>
              <DrawItem type="porkchop" x="-30" y="250" z="-4"/>
              <DrawItem type="melon" x="11" y="250" z="19"/>
              <DrawItem type="melon" x="36" y="250" z="2"/>
              <DrawItem type="carrot" x="32" y="250" z="-41"/>
              <DrawItem type="cookie" x="32" y="250" z="-39"/>
              <DrawItem type="melon" x="26" y="250" z="-27"/>
              <DrawItem type="mutton" x="46" y="250" z="-12"/>
              <DrawItem type="porkchop" x="32" y="250" z="-41"/>
              <DrawItem type="potato" x="-40" y="250" z="11"/>
              <DrawItem type="egg" x="-1" y="250" z="-13"/>
              <DrawItem type="fish" x="4" y="250" z="2"/>
              <DrawItem type="chicken" x="-9" y="250" z="22"/>
              <DrawItem type="pumpkin_pie" x="31" y="250" z="5"/>
              <DrawItem type="apple" x="-13" y="250" z="-38"/>
              <DrawItem type="rabbit" x="4" y="250" z="38"/>
              <DrawItem type="potato" x="-2" y="250" z="45"/>
              <DrawItem type="potato" x="7" y="250" z="-18"/>
              <DrawItem type="sugar" x="-34" y="250" z="45"/>
              <DrawItem type="sugar" x="31" y="250" z="-30"/>
              <DrawItem type="egg" x="-26" y="250" z="29"/>
              <DrawItem type="potato" x="13" y="250" z="37"/>
              <DrawItem type="beef" x="-45" y="250" z="-33"/>
              <DrawItem type="carrot" x="20" y="250" z="29"/>
              <DrawItem type="potato" x="-48" y="250" z="-41"/>
              <DrawItem type="sugar" x="-11" y="250" z="-22"/>
              <DrawItem type="melon" x="-48" y="250" z="25"/>
              <DrawItem type="egg" x="-32" y="250" z="-24"/>
              <DrawItem type="chicken" x="-46" y="250" z="-12"/>
              <DrawItem type="sugar" x="17" y="250" z="34"/>
              <DrawItem type="mutton" x="-37" y="250" z="-44"/>
              <DrawItem type="carrot" x="-15" y="250" z="26"/>
              <DrawItem type="egg" x="-48" y="250" z="40"/>
              <DrawItem type="melon" x="-22" y="250" z="-6"/>
              <DrawItem type="sugar" x="-4" y="250" z="33"/>
              <DrawItem type="pumpkin_pie" x="24" y="250" z="29"/>
              <DrawItem type="beef" x="-16" y="250" z="22"/>
              <DrawItem type="beef" x="-50" y="250" z="6"/>
              <DrawItem type="porkchop" x="19" y="250" z="30"/>
              <DrawItem type="carrot" x="-49" y="250" z="-32"/>
              <DrawItem type="cookie" x="3" y="250" z="-27"/>
              <DrawItem type="melon" x="46" y="250" z="13"/>
              <DrawItem type="porkchop" x="-32" y="250" z="-3"/>
              <DrawItem type="mutton" x="-33" y="250" z="-40"/>
              <DrawItem type="cookie" x="43" y="250" z="7"/>
              <DrawItem type="carrot" x="32" y="250" z="-13"/>
              <DrawItem type="chicken" x="-50" y="250" z="-50"/>
              <DrawItem type="cookie" x="32" y="250" z="-15"/>
              <DrawItem type="sugar" x="30" y="250" z="34"/>
              <DrawItem type="mutton" x="-7" y="250" z="8"/>
              <DrawItem type="chicken" x="31" y="250" z="-42"/>
              <DrawItem type="chicken" x="-36" y="250" z="31"/>
              <DrawItem type="egg" x="-5" y="250" z="49"/>
              <DrawItem type="cookie" x="-31" y="250" z="-45"/>
              <DrawItem type="carrot" x="38" y="250" z="50"/>
              <DrawItem type="chicken" x="0" y="250" z="26"/>
              <DrawItem type="apple" x="43" y="250" z="1"/>
              <DrawItem type="beef" x="-46" y="250" z="30"/>
              <DrawItem type="sugar" x="16" y="250" z="24"/>
              <DrawItem type="beef" x="-50" y="250" z="21"/>
              <DrawItem type="sugar" x="-14" y="250" z="20"/>
              <DrawItem type="mutton" x="-29" y="250" z="24"/>
              <DrawItem type="melon" x="-26" y="250" z="24"/>
              <DrawItem type="beef" x="-2" y="250" z="-16"/>
              <DrawItem type="melon" x="-30" y="250" z="42"/>
              <DrawItem type="rabbit" x="38" y="250" z="-48"/>
              <DrawItem type="rabbit" x="35" y="250" z="5"/>
              <DrawItem type="carrot" x="-11" y="250" z="-25"/>
              <DrawItem type="porkchop" x="30" y="250" z="-27"/>
              <DrawItem type="carrot" x="-6" y="250" z="-37"/>
              <DrawItem type="carrot" x="-42" y="250" z="22"/>
              <DrawItem type="egg" x="50" y="250" z="-5"/>
              <DrawItem type="carrot" x="20" y="250" z="-5"/>
              <DrawItem type="beef" x="19" y="250" z="33"/>
              <DrawItem type="cookie" x="-28" y="250" z="17"/>
              <DrawItem type="mutton" x="25" y="250" z="16"/>
              <DrawItem type="cake" x="-23" y="250" z="-26"/>
              <DrawItem type="rabbit" x="49" y="250" z="11"/>
              <DrawItem type="potato" x="-36" y="250" z="-13"/>
              <DrawItem type="egg" x="5" y="250" z="18"/>
              <DrawItem type="cake" x="30" y="250" z="21"/>
              <DrawItem type="porkchop" x="46" y="250" z="-49"/>
              <DrawItem type="potato" x="-1" y="250" z="6"/>
              <DrawItem type="sugar" x="-4" y="250" z="20"/>
              <DrawItem type="cookie" x="-22" y="250" z="-44"/>
              <DrawItem type="cookie" x="-43" y="250" z="-20"/>
              <DrawItem type="rabbit" x="27" y="250" z="23"/>
              <DrawItem type="porkchop" x="12" y="250" z="32"/>
              <DrawItem type="melon" x="10" y="250" z="-22"/>
              <DrawItem type="potato" x="6" y="250" z="-38"/>
              <DrawItem type="cookie" x="-1" y="250" z="17"/>
              <DrawItem type="mutton" x="-36" y="250" z="-21"/>
              <DrawItem type="cake" x="5" y="250" z="37"/>
              <DrawItem type="beef" x="26" y="250" z="-49"/>
              <DrawItem type="fish" x="25" y="250" z="-34"/>
              <DrawItem type="melon" x="30" y="250" z="23"/>
              <DrawItem type="sugar" x="-33" y="250" z="35"/>
              <DrawItem type="carrot" x="-34" y="250" z="-11"/>
              <DrawItem type="beef" x="32" y="250" z="-38"/>
              <DrawItem type="egg" x="40" y="250" z="20"/>
              <DrawItem type="pumpkin_pie" x="26" y="250" z="-27"/>
              <DrawItem type="mutton" x="23" y="250" z="-35"/>
              <DrawItem type="cookie" x="26" y="250" z="15"/>
              <DrawItem type="rabbit" x="-43" y="250" z="33"/>
              <DrawItem type="cake" x="8" y="250" z="-46"/>
              <DrawItem type="fish" x="12" y="250" z="34"/>
              <DrawItem type="beef" x="-26" y="250" z="-23"/>
              <DrawItem type="chicken" x="-9" y="250" z="-3"/>
              <DrawItem type="porkchop" x="-5" y="250" z="42"/>
              <DrawItem type="rabbit" x="-18" y="250" z="-48"/>
              <DrawItem type="apple" x="16" y="250" z="50"/>
              <DrawItem type="cake" x="-37" y="250" z="-40"/>
              <DrawItem type="carrot" x="-42" y="250" z="18"/>
              <DrawItem type="cake" x="-13" y="250" z="26"/>
              <DrawItem type="beef" x="-17" y="250" z="3"/>
              <DrawItem type="potato" x="50" y="250" z="-20"/>
              <DrawItem type="beef" x="20" y="250" z="-26"/>
              <DrawItem type="cake" x="50" y="250" z="-28"/>
              <DrawItem type="porkchop" x="-49" y="250" z="-24"/>
              <DrawItem type="pumpkin_pie" x="9" y="250" z="-33"/>
              <DrawItem type="potato" x="0" y="250" z="1"/>
              <DrawItem type="carrot" x="-7" y="250" z="-47"/>
              <DrawItem type="mutton" x="21" y="250" z="37"/>
              <DrawItem type="cake" x="25" y="250" z="-32"/>
              <DrawItem type="chicken" x="6" y="250" z="23"/>
              <DrawItem type="fish" x="-28" y="250" z="-17"/>
              <DrawItem type="potato" x="-45" y="250" z="-46"/>
              <DrawItem type="beef" x="-28" y="250" z="1"/>
              <DrawItem type="cookie" x="-11" y="250" z="-14"/>
              <DrawItem type="pumpkin_pie" x="-28" y="250" z="21"/>
              <DrawItem type="mutton" x="11" y="250" z="14"/>
              <DrawItem type="carrot" x="12" y="250" z="41"/>
              <DrawItem type="cookie" x="13" y="250" z="-31"/>
              <DrawItem type="pumpkin_pie" x="-29" y="250" z="47"/>
              <DrawItem type="melon" x="-4" y="250" z="45"/>
              <DrawItem type="beef" x="-41" y="250" z="-37"/>
              <DrawItem type="potato" x="50" y="250" z="33"/>
              <DrawItem type="porkchop" x="-33" y="250" z="-31"/>
              <DrawItem type="pumpkin_pie" x="19" y="250" z="3"/>
              <DrawItem type="mutton" x="-10" y="250" z="-35"/>
              <DrawItem type="cookie" x="46" y="250" z="2"/>
              <DrawItem type="carrot" x="2" y="250" z="40"/>
              <DrawItem type="chicken" x="0" y="250" z="2"/>
              <DrawItem type="pumpkin_pie" x="13" y="250" z="-5"/>
              <DrawItem type="beef" x="15" y="250" z="41"/>
              <DrawItem type="rabbit" x="-24" y="250" z="-9"/>
              <DrawItem type="melon" x="-14" y="250" z="-33"/>
              <DrawItem type="beef" x="10" y="250" z="-11"/>
              <DrawItem type="pumpkin_pie" x="25" y="250" z="8"/>
              <DrawItem type="porkchop" x="-30" y="250" z="11"/>
              <DrawItem type="fish" x="23" y="250" z="6"/>
              <DrawItem type="pumpkin_pie" x="-13" y="250" z="41"/>
              <DrawItem type="fish" x="40" y="250" z="-43"/>
              <DrawItem type="egg" x="-20" y="250" z="31"/>
              <DrawItem type="apple" x="-38" y="250" z="-47"/>
              <DrawItem type="rabbit" x="-5" y="250" z="-28"/>
              <DrawItem type="pumpkin_pie" x="18" y="250" z="23"/>
              <DrawItem type="melon" x="-29" y="250" z="-19"/>
              <DrawItem type="beef" x="-35" y="250" z="0"/>
              <DrawItem type="cookie" x="-12" y="250" z="10"/>
              <DrawItem type="potato" x="28" y="250" z="36"/>
              <DrawItem type="mutton" x="31" y="250" z="9"/>
              <DrawItem type="pumpkin_pie" x="-39" y="250" z="-23"/>
              <DrawItem type="rabbit" x="-21" y="250" z="-27"/>
              <DrawItem type="potato" x="8" y="250" z="34"/>
              <DrawItem type="mutton" x="1" y="250" z="12"/>
              <DrawItem type="melon" x="1" y="250" z="-27"/>
              <DrawItem type="egg" x="22" y="250" z="28"/>
              <DrawItem type="cookie" x="-47" y="250" z="-25"/>
              <DrawItem type="mutton" x="-11" y="250" z="14"/>
              <DrawItem type="apple" x="20" y="250" z="4"/>
              <DrawItem type="pumpkin_pie" x="-31" y="250" z="44"/>
              <DrawItem type="sugar" x="-14" y="250" z="-45"/>
              <DrawItem type="porkchop" x="24" y="250" z="19"/>
              <DrawItem type="beef" x="40" y="250" z="-1"/>
              <DrawItem type="mutton" x="37" y="250" z="0"/>
              <DrawItem type="cookie" x="-48" y="250" z="-23"/>
              <DrawItem type="rabbit" x="-15" y="250" z="23"/>
              <DrawItem type="carrot" x="13" y="250" z="-11"/>
              <DrawItem type="potato" x="4" y="250" z="31"/>
              <DrawItem type="fish" x="29" y="250" z="-18"/>
              <DrawItem type="rabbit" x="-41" y="250" z="41"/>
              <DrawItem type="egg" x="16" y="250" z="13"/>
              <DrawItem type="melon" x="-41" y="250" z="-40"/>
              <DrawItem type="chicken" x="7" y="250" z="20"/>
              <DrawItem type="apple" x="17" y="250" z="-43"/>
              <DrawItem type="carrot" x="34" y="250" z="23"/>
              <DrawItem type="melon" x="-49" y="250" z="-5"/>
              <DrawItem type="potato" x="-39" y="250" z="18"/>
              <DrawItem type="porkchop" x="-39" y="250" z="-15"/>
              <DrawItem type="rabbit" x="44" y="250" z="34"/>
              <DrawItem type="fish" x="-35" y="250" z="34"/>
              <DrawItem type="sugar" x="43" y="250" z="46"/>
              <DrawItem type="apple" x="-6" y="250" z="31"/>
              <DrawItem type="rabbit" x="13" y="250" z="5"/>
              <DrawItem type="egg" x="-17" y="250" z="-33"/>
              <DrawItem type="porkchop" x="-2" y="250" z="14"/>
              <DrawItem type="porkchop" x="31" y="250" z="-22"/>
              <DrawItem type="melon" x="46" y="250" z="-35"/>
              <DrawItem type="porkchop" x="-42" y="250" z="-23"/>
              <DrawItem type="cake" x="-45" y="250" z="-42"/>
              <DrawItem type="cookie" x="5" y="250" z="-2"/>
              <DrawItem type="fish" x="47" y="250" z="29"/>
              <DrawItem type="fish" x="39" y="250" z="-20"/>
              <DrawItem type="cake" x="-29" y="250" z="16"/>
              <DrawItem type="carrot" x="33" y="250" z="8"/>
              <DrawItem type="fish" x="-47" y="250" z="6"/>
              <DrawItem type="cookie" x="-2" y="250" z="13"/>
              <DrawItem type="pumpkin_pie" x="25" y="250" z="-2"/>
              <DrawItem type="apple" x="-39" y="250" z="23"/>
              <DrawItem type="fish" x="37" y="250" z="4"/>
              <DrawItem type="fish" x="8" y="250" z="37"/>
              <DrawItem type="cookie" x="-29" y="250" z="38"/>
              <DrawItem type="cookie" x="-39" y="250" z="-5"/>
              <DrawItem type="pumpkin_pie" x="17" y="250" z="-38"/>
              <DrawItem type="carrot" x="-38" y="250" z="-34"/>
              <DrawItem type="porkchop" x="-17" y="250" z="2"/>
              <DrawItem type="pumpkin_pie" x="6" y="250" z="0"/>
              <DrawItem type="beef" x="43" y="250" z="-36"/>
              <DrawItem type="carrot" x="1" y="250" z="3"/>
              <DrawItem type="apple" x="-23" y="250" z="-14"/>
              <DrawItem type="mutton" x="-19" y="250" z="30"/>
              <DrawItem type="fish" x="12" y="250" z="-3"/>
              <DrawItem type="porkchop" x="38" y="250" z="14"/>
              <DrawItem type="apple" x="7" y="250" z="28"/>
              <DrawItem type="cake" x="9" y="250" z="-5"/>
              <DrawItem type="melon" x="-49" y="250" z="22"/>
              <DrawItem type="fish" x="-39" y="250" z="-42"/>
              <DrawItem type="rabbit" x="23" y="250" z="22"/>
              <DrawItem type="rabbit" x="8" y="250" z="-14"/>
              <DrawItem type="chicken" x="-10" y="250" z="-19"/>
              <DrawItem type="porkchop" x="-1" y="250" z="8"/>
              <DrawItem type="pumpkin_pie" x="8" y="250" z="23"/>
              <DrawItem type="cookie" x="34" y="250" z="-1"/>
              <DrawItem type="carrot" x="32" y="250" z="-5"/>
              <DrawItem type="egg" x="50" y="250" z="-29"/>
              <DrawItem type="cake" x="40" y="250" z="31"/>
              <DrawItem type="pumpkin_pie" x="48" y="250" z="23"/>
              <DrawItem type="rabbit" x="36" y="250" z="17"/>
              <DrawItem type="sugar" x="-10" y="250" z="-31"/>
              <DrawItem type="mutton" x="-25" y="250" z="-31"/>
              <DrawItem type="egg" x="33" y="250" z="42"/>
              <DrawItem type="fish" x="-23" y="250" z="-8"/>
              <DrawItem type="rabbit" x="27" y="250" z="32"/>
              <DrawItem type="apple" x="-41" y="250" z="-37"/>
              <DrawItem type="egg" x="40" y="250" z="-17"/>
              <DrawItem type="apple" x="-41" y="250" z="-32"/>
              <DrawItem type="carrot" x="-16" y="250" z="42"/>
              <DrawItem type="cake" x="-16" y="250" z="45"/>
              <DrawItem type="mutton" x="-35" y="250" z="38"/>
              <DrawItem type="fish" x="-45" y="250" z="38"/>
              <DrawItem type="apple" x="-7" y="250" z="31"/>
              <DrawItem type="apple" x="0" y="250" z="-36"/>
              <DrawItem type="mutton" x="-46" y="250" z="2"/>
              <DrawItem type="cake" x="28" y="250" z="46"/>
              <DrawItem type="melon" x="33" y="250" z="-38"/>
              <DrawItem type="fish" x="37" y="250" z="-23"/>
              <DrawItem type="chicken" x="-32" y="250" z="-46"/>
              <DrawItem type="potato" x="26" y="250" z="-44"/>
              <DrawItem type="melon" x="-16" y="250" z="-48"/>
              <DrawItem type="porkchop" x="50" y="250" z="44"/>
              <DrawItem type="mutton" x="-34" y="250" z="-50"/>
              <DrawItem type="pumpkin_pie" x="38" y="250" z="24"/>
              <DrawItem type="mutton" x="-10" y="250" z="-1"/>
              <DrawItem type="pumpkin_pie" x="41" y="250" z="-10"/>
              <DrawItem type="beef" x="2" y="250" z="-50"/>
              <DrawItem type="sugar" x="42" y="250" z="-50"/>
              <DrawItem type="beef" x="-47" y="250" z="20"/>
              <DrawItem type="mutton" x="-22" y="250" z="46"/>
              <DrawItem type="cookie" x="28" y="250" z="-48"/>
              <DrawItem type="mutton" x="-7" y="250" z="20"/>
              <DrawItem type="egg" x="48" y="250" z="41"/>
              <DrawItem type="egg" x="49" y="250" z="27"/>
              <DrawItem type="apple" x="-20" y="250" z="14"/>
              <DrawItem type="fish" x="-13" y="250" z="-21"/>
              <DrawItem type="carrot" x="-12" y="250" z="-24"/>
              <DrawItem type="rabbit" x="-7" y="250" z="9"/>
              <DrawItem type="pumpkin_pie" x="15" y="250" z="48"/>
              <DrawItem type="beef" x="30" y="250" z="-23"/>
              <DrawItem type="cookie" x="50" y="250" z="5"/>
              <DrawItem type="chicken" x="-33" y="250" z="-25"/>
              <DrawItem type="cake" x="18" y="250" z="-13"/>
            </DrawingDecorator>
            <ServerQuitFromTimeUp description="" timeLimitMs="15000"/>
            <ServerQuitWhenAnyAgentFinishes description=""/>
          </ServerHandlers>
        </ServerSection>
        
        <AgentSection mode="Survival">
          <Name>The Hungry Caterpillar</Name>
          <AgentStart>
            <Placement pitch="0" x="0.5" y="227.0" yaw="0" z="0.5"/>
            <Inventory/>
          </AgentStart>
          <AgentHandlers>
            <VideoProducer want_depth="false">
              <Width>480</Width>
              <Height>320</Height>
            </VideoProducer>
            <ObservationFromFullStats />
            <RewardForCollectingItem>
              <Item reward="2" type="fish porkchop beef chicken rabbit mutton"/>
              <Item reward="1" type="potato egg carrot"/>
              <Item reward="-1" type="apple melon"/>
              <Item reward="-2" type="sugar cake cookie pumpkin_pie"/>
            </RewardForCollectingItem>
            <ContinuousMovementCommands turnSpeedDegs="240">
              <ModifierList type="deny-list">
                <command>attack</command>
              </ModifierList>
            </ContinuousMovementCommands>
          </AgentHandlers>
        </AgentSection>
      </Mission>'''