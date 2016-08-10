#!/usr/bin/python
import argparse
import logging
import time
import sys
import json
import configparser
from POGOProtos.Enums import PokemonMove_pb2
from custom_exceptions import GeneralPogoException

from api import PokeAuthSession
from location import Location

from pokedex import pokedex
from inventory import items
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
from flask import jsonify
import thread
import subprocess
import os
import sys


app = Flask(__name__)


@app.route('/release')
def release():
    inventory = session.getInventory()
    
    #id: 2436312686824190668
    #pokemon_id: EEVEE
    #cp: 46
    #stamina: 19
    #stamina_max: 19
    #move_1: TACKLE_FAST
    #move_2: DIG
    #height_m: 0.297532558441
    #weight_kg: 8.24643802643
    #individual_attack: 15
    #individual_defense: 12
    #individual_stamina: 9
    #cp_multiplier: 0.166397869587
    #pokeball: ITEM_POKE_BALL
    #captured_cell_id: 6108423709528162304
    #creation_time_ms: 1469364470778
    pokeID = request.args.get('pokeID', 0)
    action = request.args.get('action',0)
    
    
    
    
    for z in pokeID.split(","):
        
    
        for poke in range(0,len(inventory.party)-1):
            curPoke = inventory.party[poke]
            #logging.critical(str(curPoke.id) + "," + str(z))
            
            if str(curPoke.id) == str(z):
                iv = (round(inventory.party[poke].individual_attack + inventory.party[poke].individual_defense + inventory.party[poke].individual_stamina) / 45)
                
                #logging.critical(inventory.party[poke].individual_attack)
                #logging.critical(inventory.party[poke].individual_defense)
                #logging.critical(inventory.party[poke].individual_stamina)
                #logging.critical(iv)
                #logging.critical(iv*100)
                #logging.critical(int(iv*100))
                
                if action.find("Release") > -1:
                    logging.critical("Found pokemon. Transfer in progress...")
                    logging.critical(session.releasePokemon(inventory.party[poke]))
                elif action.find("Evolve") > -1:
                    logging.critical("Found pokemon. Evolve in progress...")
                    logging.critical(session.evolvePokemon(inventory.party[poke]))
                elif action.find("Rename") > -1:
                    logging.critical("Found pokemon. Renaming to " + str(pokedex[curPoke.pokemon_id]) + str(int(iv*100)))
                    logging.critical(session.nicknamePokemon(inventory.party[poke],str(pokedex[curPoke.pokemon_id]) + str(int(iv*100))))
                    #logging.critical(inventory.party)
                time.sleep(1)
    return render_template('inventoryTimeout.html')
    

@app.route('/inventory')
def inventory():
    inventory = session.getInventory()
    pokes = []
    #id: 2436312686824190668
    #pokemon_id: EEVEE
    #cp: 46
    #stamina: 19
    #stamina_max: 19
    #move_1: TACKLE_FAST
    #move_2: DIG
    #height_m: 0.297532558441
    #weight_kg: 8.24643802643
    #individual_attack: 15
    #individual_defense: 12
    #individual_stamina: 9
    #cp_multiplier: 0.166397869587
    #pokeball: ITEM_POKE_BALL
    #captured_cell_id: 6108423709528162304
    #creation_time_ms: 1469364470778
    
    
    for poke in range(0,len(inventory.party)):
        
    
        family = {'1': {1,2,3},'4': {4,5,6},'7': {7,8,9}, '10': {10,11,12}, '13': {13,14,15}, '16': {16,17,18}, '19': {19,20}, '21': {21,22}, '23': {23,24},'25': {25,26}, '27': {27,28}, '29': {29,30,31}, '32': {32,33,34}, '35': {35,36}, '37': {37,38}, '39': {39,40}, '41': {41,42}, '43': {43,44,45}, '46': {46,47}, '48': {48,49}, '50': {50,51}, '52': {52,53},'54': {54,55}, '56': {56,57}, '58': {58,59}, '60': {60,61,62}, '63': {63,64,65}, '66': {66,67,68},'69': {69,70,71}, '72': {72,73}, '74': {74,75,76}, '77': {77,78}, '79': {79,80}, '81': {81,82,83}, '84': {84,85}, '86': {86,87}, '88': {88,89}, '90': {90,91}, '92': {92,93,94}, '95': {95}, '96': {96,97}, '98': {98,99}, '100': {100,101}, '102': {102,103}, '104': {104,105}, '106': {106}, '107': {107},'108': {108}, '109': {109,110}, '111': {111,112}, '113': {113}, '114': {114}, '115': {115}, '116': {116,117}, '118': {118,119}, '120': {120,121},'122': {122}, '123': {123}, '124': {124}, '125': {125}, '126': {126}, '127': {127}, '128': {128}, '129': {129,130}, '131': {131}, '132': {132}, '133': {133,134,135,136},'137': {137}, '138': {138,139}, '140': {140,141},'142': {142}, '143': {143}, '144': {144}, '145': {145}, '146':{146}, '147': {147,148,149}, '150': {150}, '151': {151}}
        reqCandy = {'1':25,'2':100,'3':0,'4':25,'5':100,'6':0,'7':25,'8':100,'9':0,'10':12,'11':50,'12':0,'13':12,'14':50,'15':0,'16':12,'17':50,'18':0,'19':25,'20':0,'21':50,'22':0,'23':50,'24':0,'25':50,'26':0,'27':50,'28':0,'29':25,'30':100,'31':0,'32':25,'33':100,'34':0,'35':50,'36':0,'37':50,'38':0,'39':50,'40':0,'41':50,'42':0,'43':25,'44':100,'45':0,'46':50,'47':0,'48':50,'49':0,'50':50,'51':0,'52':50,'53':0,'54':50,'55':0,'56':50,'57':0,'58':50,'59':0,'60':25,'61':100,'62':0,'63':25,'64':100,'65':0,'66':25,'67':100,'68':0,'69':25,'70':100,'71':0,'72':50,'73':0,'74':25,'75':100,'76':0,'77':50,'78':0,'79':50,'80':0,'81':50,'82':0,'83':0,'84':50,'85':0,'86':50,'87':0,'88':50,'89':0,'90':50,'91':0,'92':25,'93':100,'94':0,'95':0,'96':50,'97':0,'98':50,'99':0,'100':50,'101':0,'102':50,'103':0,'104':50,'105':0,'106':0,'107':0,'108':0,'109':50,'110':0,'111':50,'112':0,'113':0,'114':0,'115':0,'116':50,'117':0,'118':50,'119':0,'120':50,'121':0,'122':0,'123':0,'124':0,'125':0,'126':0,'127':0,'128':0,'129':400,'130':0,'131':0,'132':0,'133':25,'134':0,'135':0,'136':0,'137':0,'138':50,'139':0,'140':50,'141':0,'142':0,'143':0,'144':0,'145':0,'146':0,'147':25,'148':100,'149':0,'150':0,'151':0}
        
        curPoke = inventory.party[poke]   
        candies = 0
        if str(curPoke.pokemon_id) not in family:
            
            for z in family:
                
                if curPoke.pokemon_id in family[z]:
                    #logging.critical(str(pokedex[curPoke.pokemon_id]) + " is in family " +str(z))
                    #logging.critical(inventory.candies)
                    candies = inventory.candies[int(z)]
        else:
            #logging.critical(str(curPoke.pokemon_id) + " is a family!")
            candies = inventory.candies[curPoke.pokemon_id]
        
            
        pokez = {
        'id': str(curPoke.id),
        'pokemon_id': curPoke.pokemon_id,
        'pokemon_name': pokedex[curPoke.pokemon_id],
        'cp': curPoke.cp,
        'stamina': curPoke.stamina,
        'stamina_max': curPoke.stamina_max,
        'move_1': curPoke.move_1,
        'move_2': curPoke.move_2,
        'height_m': curPoke.height_m,
        'weight_kg': curPoke.weight_kg,
        'individual_attack': curPoke.individual_attack,
        'individual_defense': curPoke.individual_defense,
        'individual_stamina': curPoke.individual_stamina,
        'candies': candies,
        'reqCandies': reqCandy[str(curPoke.pokemon_id)]
        }
        pokes.append(pokez)
        
        
    
    
    
    json.dump(pokes, open('static/inventory.json', 'w'))
    
    return render_template('inventory.html')
    
@app.route('/')
def index():
    
    stats = session.getInventory().stats
    profileInfo = session.getProfile().player_data

        #level
        #experience: 2004695
        #prev_level_xp: 1650000
        #next_level_xp: 2500000
        #km_walked: 29.3902397156
        #pokemons_encountered: 4484
        #unique_pokedex_entries: 92
        #pokemons_captured: 4348
        #evolutions: 614
        #poke_stop_visits: 13337
        #pokeballs_thrown: 4819
        #eggs_hatched: 7
    
    
    if profileInfo.team:
        
        team = profileInfo.team
    else:
        team = 'noteam'
               
    statz = {
    'level': str(stats.level),
    'experience': str(stats.experience),
    'next_level_xp': str(stats.next_level_xp),
    'km_walked': str(stats.km_walked),
    'pokemons_encountered': str(stats.pokemons_encountered),
    'pokemons_captured': str(stats.pokemons_captured),
    'username': str(profileInfo.username),
    'max_pokemon_storage': str(profileInfo.max_pokemon_storage),
    'max_item_storage': str(profileInfo.max_item_storage),
    'team': team
     }

    json.dump(statz, open('static/stats.json', 'w'))
    

    return render_template('dashboard.html')
    


@app.errorhandler(500)
def page_not_found(e):
    return render_template('result.html'), 404

    
def setupLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('Line %(lineno)d,%(filename)s - %(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)



# Get profile
def getProfile(session):
        logging.info("Printing Profile:")
        profile = session.getProfile()
        logging.info(profile)



# Do Inventory stuff
def getInventory(session):
    logging.info("Get Inventory:")
    logging.info(session.getInventory())



if __name__ == '__main__':
    data = [{'status':'Server startup. Nothing to report.'}]
    json.dump(data, open('static/catch_data.json', 'w'))
    time.sleep(1)
    setupLogger()
    logging.debug('Logger set up')

    	
	#parse in configuration from config.ini
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    #config.get('AUTH','type')
    #config.get('AUTH','username')
    #config.get('AUTH','password')
    #config.get('CONFIG','startLoc')
    #config.get('CONFIG','minCP')
    
    # Check service
    minCP = int(config.get('CONFIG','minCP'))
    if config.get('AUTH','type') not in ['ptc', 'google']:
        logging.error('Invalid auth service {}'.format(config.get('AUTH','type')))
        sys.exit(-1)

    # Create PokoAuthObject
    poko_session = PokeAuthSession(
        config.get('AUTH','username'),
        config.get('AUTH','password'),
        config.get('AUTH','type'),
        ''.join(['encrypt/',config.get('CONFIG', 'encryptFile')]),
        geo_key=""
    )

    # Authenticate with a given location
    # Location is not inherent in authentication
    # But is important to session
    if config.get('CONFIG','startLoc'):
        session = poko_session.authenticate(locationLookup=config.get('CONFIG','startLoc'))
    else:
        session = poko_session.authenticate()

    # Time to show off what we can do
    logging.info("Successfully logged in to Pokemon Go! Starting web server on port 5100.")
    
    app.run(host='0.0.0.0', port=5100, debug=True)
    url_for('static', filename='catch_data.json')
    	
    
	
