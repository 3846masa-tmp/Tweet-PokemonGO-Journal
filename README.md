# Tweet PokemonGO Journal powered by pgoapi
Tweet PokemonGO Journal powered by pgoapi https://github.com/tejado/pgoapi.  

 * This is unofficial - USE AT YOUR OWN RISK !
 * This is Japanese.

## Supports
 * Python 3
 * Uses [POGOProtos](https://github.com/AeonLucid/POGOProtos)
 * Following Journal:
   * fort_search
   * catch_pokemon

## Usage

### with Docker
Build and run container:

    docker build -t tweet_pokego .
    docker run --rm --restart always -e TZ="Asia/Tokyo" -v ${PWD}/config.json:/config.json tweet_pokego

## Requirements
 * Python 3
 * requests
 * protobuf (>=3)
 * gpsoauth
 * geopy (only for pokecli demo)
 * s2sphere (only for pokecli demo)
 * tweepy

## Credits
https://github.com/tejado/pgoapi#credits
