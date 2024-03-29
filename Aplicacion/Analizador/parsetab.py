
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ARCHIVO BACKUP BODY CLOUD CONFIGURE COPY CREATE DELETE ENCRYPTLOG ENCRYPTREAD EXEC FALSE FROM LLAVE LOCAL MODE MODIFY NAME PATH RENAME RUTA STRING TO TRANSFER TRUE TYPEinicio : lexico\n    lexico : lexico comandos\n                | comandos\n    comandos : maincomando subcomando\n                | maincomando\n    maincomando : CONFIGURE \n                | CREATE\n                | DELETE\n                | COPY\n                | TRANSFER\n                | RENAME\n                | MODIFY\n                | ADD\n                | BACKUP\n                | EXEC\n    subcomando : subcomando sub\n                    | sub\n    sub : TYPE tipo\n                    | ENCRYPTLOG encriptado\n                    | ENCRYPTREAD encriptado\n                    | LLAVE STRING\n                    | NAME name\n                    | BODY STRING\n                    | PATH RUTA\n                    | FROM RUTA\n                    | TO RUTA\n                    | MODE tipo\n    tipo : LOCAL\n            | CLOUD\n    encriptado : TRUE\n            | FALSE\n    name : ARCHIVO\n    '
    
_lr_action_items = {'CONFIGURE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[5,5,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'CREATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[6,6,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'DELETE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[7,7,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'COPY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[8,8,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'TRANSFER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[9,9,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'RENAME':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[10,10,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'MODIFY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[11,11,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'ADD':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[12,12,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'BACKUP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[13,13,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'EXEC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[14,14,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[0,-1,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'TYPE':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[18,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,18,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'ENCRYPTLOG':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[19,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,19,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'ENCRYPTREAD':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[20,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,20,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'LLAVE':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[21,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,21,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'NAME':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[22,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,22,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'BODY':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[23,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,23,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'PATH':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[24,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,24,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'FROM':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[25,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,25,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'TO':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[26,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,26,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'MODE':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[27,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,27,-17,-16,-18,-28,-29,-19,-30,-31,-20,-21,-22,-32,-23,-24,-25,-26,-27,]),'LOCAL':([18,27,],[30,30,]),'CLOUD':([18,27,],[31,31,]),'TRUE':([19,20,],[33,33,]),'FALSE':([19,20,],[34,34,]),'STRING':([21,23,],[36,39,]),'ARCHIVO':([22,],[38,]),'RUTA':([24,25,26,],[40,41,42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'lexico':([0,],[2,]),'comandos':([0,2,],[3,15,]),'maincomando':([0,2,],[4,4,]),'subcomando':([4,],[16,]),'sub':([4,16,],[17,28,]),'tipo':([18,27,],[29,43,]),'encriptado':([19,20,],[32,35,]),'name':([22,],[37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> lexico','inicio',1,'p_inicio','gramar.py',135),
  ('lexico -> lexico comandos','lexico',2,'p_lexico','gramar.py',142),
  ('lexico -> comandos','lexico',1,'p_lexico','gramar.py',143),
  ('comandos -> maincomando subcomando','comandos',2,'p_comandos','gramar.py',153),
  ('comandos -> maincomando','comandos',1,'p_comandos','gramar.py',154),
  ('maincomando -> CONFIGURE','maincomando',1,'p_main_comando','gramar.py',170),
  ('maincomando -> CREATE','maincomando',1,'p_main_comando','gramar.py',171),
  ('maincomando -> DELETE','maincomando',1,'p_main_comando','gramar.py',172),
  ('maincomando -> COPY','maincomando',1,'p_main_comando','gramar.py',173),
  ('maincomando -> TRANSFER','maincomando',1,'p_main_comando','gramar.py',174),
  ('maincomando -> RENAME','maincomando',1,'p_main_comando','gramar.py',175),
  ('maincomando -> MODIFY','maincomando',1,'p_main_comando','gramar.py',176),
  ('maincomando -> ADD','maincomando',1,'p_main_comando','gramar.py',177),
  ('maincomando -> BACKUP','maincomando',1,'p_main_comando','gramar.py',178),
  ('maincomando -> EXEC','maincomando',1,'p_main_comando','gramar.py',179),
  ('subcomando -> subcomando sub','subcomando',2,'p_subcomando','gramar.py',185),
  ('subcomando -> sub','subcomando',1,'p_subcomando','gramar.py',186),
  ('sub -> TYPE tipo','sub',2,'p_sub','gramar.py',204),
  ('sub -> ENCRYPTLOG encriptado','sub',2,'p_sub','gramar.py',205),
  ('sub -> ENCRYPTREAD encriptado','sub',2,'p_sub','gramar.py',206),
  ('sub -> LLAVE STRING','sub',2,'p_sub','gramar.py',207),
  ('sub -> NAME name','sub',2,'p_sub','gramar.py',208),
  ('sub -> BODY STRING','sub',2,'p_sub','gramar.py',209),
  ('sub -> PATH RUTA','sub',2,'p_sub','gramar.py',210),
  ('sub -> FROM RUTA','sub',2,'p_sub','gramar.py',211),
  ('sub -> TO RUTA','sub',2,'p_sub','gramar.py',212),
  ('sub -> MODE tipo','sub',2,'p_sub','gramar.py',213),
  ('tipo -> LOCAL','tipo',1,'p_tipo','gramar.py',223),
  ('tipo -> CLOUD','tipo',1,'p_tipo','gramar.py',224),
  ('encriptado -> TRUE','encriptado',1,'p_encriptado','gramar.py',230),
  ('encriptado -> FALSE','encriptado',1,'p_encriptado','gramar.py',231),
  ('name -> ARCHIVO','name',1,'p_name','gramar.py',237),
]
