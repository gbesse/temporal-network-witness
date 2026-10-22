import argparse
import json
from pathlib import Path
import sys
from .core import run
from .metadata import DESCRIPTION

ERROR = {'fr':'Entrée invalide : vérifier les champs et les limites documentés.', 'en':'Invalid input: check documented fields and bounds.', 'es':'Entrada no válida: compruebe los campos y límites documentados.'}

def reject_constant(value):
    raise ValueError('nonfinite_json')

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('input', nargs='?')
    parser.add_argument('--lang', choices=['fr','en','es'], default='en')
    args, unknown=parser.parse_known_args()
    try:
        if unknown or not args.input: raise ValueError('arguments')
        data=json.loads(Path(args.input).read_text(), parse_constant=reject_constant)
        if not isinstance(data,dict): raise ValueError('object_required')
        result=run(data)
        print(json.dumps({'language':args.lang,'summary':DESCRIPTION[args.lang],'result':result},ensure_ascii=False,allow_nan=False,sort_keys=True))
    except (ValueError,KeyError,TypeError,OSError,OverflowError,ZeroDivisionError):
        print(json.dumps({'code':'invalid_input','message':ERROR[args.lang]},ensure_ascii=False),file=sys.stderr)
        return 2
    return 0
if __name__=='__main__': sys.exit(main())
