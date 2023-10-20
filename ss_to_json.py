import base64
import sys
import json

def ss_to_byte(clear_ss_config: str):
    bs_bytes = clear_ss_config.encode("ascii")
    return base64.b64decode(bs_bytes).decode("ascii")

def ss_okam(raw_ss_config):
    ss_text = raw_ss_config.split("#")[0] if raw_ss_config.find("#") != -1 else raw_ss_config
    #print(ss_text)
    ss_text = ss_text.split("ss://")[1] if ss_text.find("ss://") != -1 else ss_text
    #print(ss_text)
    return ss_text

def decode_ss_config_to_json(decode_ss_config: str):
    decode_ss_config = decode_ss_config.split(":")
    #print(decode_ss_config)
    return json.dumps({
      "method"   : decode_ss_config[0],
      "password" : decode_ss_config[1].split("@")[0],
      "server"   : decode_ss_config[1].split("@")[1],
      "server-port" : decode_ss_config[2]
    }, indent=4)

def ss_to_json(raw_ss_config: str):
    return decode_ss_config_to_json(ss_to_byte(ss_okam(raw_ss_config)))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        exit() 
    else:
        argvs = sys.argv[1:]
        print(ss_to_json(argvs[0]))
