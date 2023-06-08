
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ARCHIVO BACKUP BODY CLOUD CONFIGURE COPY CREATE DELETE ENCRYPTLOG ENCRYPTREAD EXEC FALSE FROM LLAVE LOCAL MODE MODIFY NAME PATH RENAME RUTA STRING TO TRANSFER TRUE TYPEinicio : lexico\n    lexico : lexico comandos\n                | comandos\n    comandos : maincomando subcomando\n    maincomando : CONFIGURE \n                | CREATE\n                | DELETE\n                | COPY\n                | TRANSFER\n                | RENAME\n                | MODIFY\n                | ADD\n                | BACKUP\n                | EXEC\n    subcomando : subcomando sub\n                    | sub\n    sub : TYPE tipo\n                    | ENCRYPTLOG encriptado\n                    | ENCRYPTREAD encriptado\n                    | LLAVE STRING\n                    | NAME ARCHIVO\n                    | BODY STRING\n                    | PATH RUTA\n                    | FROM RUTA\n                    | TO RUTA\n                    | MODE tipo\n    tipo : LOCAL\n            | CLOUD\n    encriptado : TRUE\n            | FALSE\n    '
    
_lr_action_items = {'CONFIGURE':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[5,5,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'CREATE':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[6,6,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'DELETE':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[7,7,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'COPY':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[8,8,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'TRANSFER':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[9,9,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'RENAME':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[10,10,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'MODIFY':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[11,11,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'ADD':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[12,12,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'BACKUP':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[13,13,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'EXEC':([0,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[14,14,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'$end':([1,2,3,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[0,-1,-3,-2,-4,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'TYPE':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,18,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'ENCRYPTLOG':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,19,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'ENCRYPTREAD':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[20,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,20,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'LLAVE':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[21,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,21,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'NAME':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[22,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,22,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'BODY':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[23,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,23,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'PATH':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[24,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,24,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'FROM':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[25,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,25,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'TO':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[26,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,26,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'MODE':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[27,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,27,-16,-15,-17,-27,-28,-18,-29,-30,-19,-20,-21,-22,-23,-24,-25,-26,]),'LOCAL':([18,27,],[30,30,]),'CLOUD':([18,27,],[31,31,]),'TRUE':([19,20,],[33,33,]),'FALSE':([19,20,],[34,34,]),'STRING':([21,23,],[36,38,]),'ARCHIVO':([22,],[37,]),'RUTA':([24,25,26,],[39,40,41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'lexico':([0,],[2,]),'comandos':([0,2,],[3,15,]),'maincomando':([0,2,],[4,4,]),'subcomando':([4,],[16,]),'sub':([4,16,],[17,28,]),'tipo':([18,27,],[29,42,]),'encriptado':([19,20,],[32,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> lexico','inicio',1,'p_inicio','gramar.py',97),
  ('lexico -> lexico comandos','lexico',2,'p_lexico','gramar.py',102),
  ('lexico -> comandos','lexico',1,'p_lexico','gramar.py',103),
  ('comandos -> maincomando subcomando','comandos',2,'p_comandos','gramar.py',118),
  ('maincomando -> CONFIGURE','maincomando',1,'p_main_comando','gramar.py',129),
  ('maincomando -> CREATE','maincomando',1,'p_main_comando','gramar.py',130),
  ('maincomando -> DELETE','maincomando',1,'p_main_comando','gramar.py',131),
  ('maincomando -> COPY','maincomando',1,'p_main_comando','gramar.py',132),
  ('maincomando -> TRANSFER','maincomando',1,'p_main_comando','gramar.py',133),
  ('maincomando -> RENAME','maincomando',1,'p_main_comando','gramar.py',134),
  ('maincomando -> MODIFY','maincomando',1,'p_main_comando','gramar.py',135),
  ('maincomando -> ADD','maincomando',1,'p_main_comando','gramar.py',136),
  ('maincomando -> BACKUP','maincomando',1,'p_main_comando','gramar.py',137),
  ('maincomando -> EXEC','maincomando',1,'p_main_comando','gramar.py',138),
  ('subcomando -> subcomando sub','subcomando',2,'p_subcomando','gramar.py',144),
  ('subcomando -> sub','subcomando',1,'p_subcomando','gramar.py',145),
  ('sub -> TYPE tipo','sub',2,'p_sub','gramar.py',164),
  ('sub -> ENCRYPTLOG encriptado','sub',2,'p_sub','gramar.py',165),
  ('sub -> ENCRYPTREAD encriptado','sub',2,'p_sub','gramar.py',166),
  ('sub -> LLAVE STRING','sub',2,'p_sub','gramar.py',167),
  ('sub -> NAME ARCHIVO','sub',2,'p_sub','gramar.py',168),
  ('sub -> BODY STRING','sub',2,'p_sub','gramar.py',169),
  ('sub -> PATH RUTA','sub',2,'p_sub','gramar.py',170),
  ('sub -> FROM RUTA','sub',2,'p_sub','gramar.py',171),
  ('sub -> TO RUTA','sub',2,'p_sub','gramar.py',172),
  ('sub -> MODE tipo','sub',2,'p_sub','gramar.py',173),
  ('tipo -> LOCAL','tipo',1,'p_tipo','gramar.py',183),
  ('tipo -> CLOUD','tipo',1,'p_tipo','gramar.py',184),
  ('encriptado -> TRUE','encriptado',1,'p_encriptado','gramar.py',189),
  ('encriptado -> FALSE','encriptado',1,'p_encriptado','gramar.py',190),
]
