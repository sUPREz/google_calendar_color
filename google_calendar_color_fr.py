from enum import Enum

class ColorType(Enum):
  COLOR_TYPE_CALENDAR = 0
  COLOR_TYPE_EVENT = 1

class CalendarColor(Enum):
  CACAO = 1
  ROSE_CLAIR = 2
  TOMATE = 3
  MANDARINE = 4
  CIRTOUILLE = 5
  MANGUE = 6
  EUCALYPTUS = 7
  BASILIC = 8
  PISTACHE = 9
  AVOCAT = 10
  CITRON = 11
  BANANE = 12
  SAUGE = 13
  PAON = 14
  COBALT = 15
  MYRTILLE = 16
  LAVANDE = 17
  GLYCINE = 18
  ANTHRACITE = 19
  GRIS_TAUPE = 20
  MAGENTA = 21
  VIEUX_ROSE = 22
  RAISIN = 23
  AMETHYSTE = 24
  
class EventColor(Enum):
  LAVANDE = 1
  SAUGE = 2
  RAISIN = 3
  FLAMANT_ROSE = 4
  BANANE = 5
  MANDARINE = 6
  PAON = 7
  GRAPHITE = 8
  MYRTILLE = 9
  BASILIC = 10
  TOMATE = 11

class GoogleCalendarColor():
  def __init__(
      self, 
      _color_name : str , 
      _color_type : ColorType , 
      _api_color : str,
      _web_color : str,
      _android_color : str
      ) -> None:
    
    self.color_name = _color_name
    self.color_type = _color_type
    self.api_color = _api_color
    self.web_color = _web_color
    self.android_color = _android_color

    self.color = self.android_color
    
    pass

calendar_color_list = {
  CalendarColor.MAGENTA : GoogleCalendarColor("Magenta"        ,ColorType.COLOR_TYPE_CALENDAR,"ac725e","ad1457","c25978"),
  CalendarColor.VIEUX_ROSE : GoogleCalendarColor("Vieux Rose"  ,ColorType.COLOR_TYPE_CALENDAR,"cca6ac","d81b60","dd5c7a"),
  CalendarColor.TOMATE : GoogleCalendarColor("Tomate"          ,ColorType.COLOR_TYPE_CALENDAR,"f83a22","d50000","d8583b"),
  CalendarColor.ROSE_CLAIR : GoogleCalendarColor("Rose Clair"  ,ColorType.COLOR_TYPE_CALENDAR,"f691b2","e67c73","d4847b"),
  CalendarColor.MANDARINE : GoogleCalendarColor("Mandariune"   ,ColorType.COLOR_TYPE_CALENDAR,"fa573c","f4511e","e16c41"),
  CalendarColor.CIRTOUILLE : GoogleCalendarColor("Citrouille"  ,ColorType.COLOR_TYPE_CALENDAR,"ff7537","ef6c00","dc7b3a"),
  CalendarColor.MANGUE : GoogleCalendarColor("Mangue"          ,ColorType.COLOR_TYPE_CALENDAR,"ffad49","f09300","de9540"),
  CalendarColor.BANANE : GoogleCalendarColor("Banane"          ,ColorType.COLOR_TYPE_CALENDAR,"fac165","f6bf26","e8bb5c"),
  CalendarColor.CITRON : GoogleCalendarColor("Citron"          ,ColorType.COLOR_TYPE_CALENDAR,"fbe983","eac441","e6bb57"),
  CalendarColor.AVOCAT : GoogleCalendarColor("Avocat"          ,ColorType.COLOR_TYPE_CALENDAR,"b3dc6c","c0ca33","bec058"),
  CalendarColor.PISTACHE : GoogleCalendarColor("Pistache"      ,ColorType.COLOR_TYPE_CALENDAR,"7bd148","7cb342","86a95c"),
  CalendarColor.SAUGE : GoogleCalendarColor("Sauge"            ,ColorType.COLOR_TYPE_CALENDAR,"42d692","33b679","58ad87"),
  CalendarColor.BASILIC : GoogleCalendarColor("Basilic"        ,ColorType.COLOR_TYPE_CALENDAR,"16a765","0b8043","4e9462"),
  CalendarColor.EUCALYPTUS : GoogleCalendarColor("Eucalyptus"  ,ColorType.COLOR_TYPE_CALENDAR,"92e1c0","009688","479b91"),
  CalendarColor.PAON : GoogleCalendarColor("Paon"              ,ColorType.COLOR_TYPE_CALENDAR,"9fe1e7","039be5","5498cf"),
  CalendarColor.COBALT : GoogleCalendarColor("Cobalt"          ,ColorType.COLOR_TYPE_CALENDAR,"9fc6e7","4285f4","6c8cdc"),
  CalendarColor.MYRTILLE : GoogleCalendarColor("Myrtille"      ,ColorType.COLOR_TYPE_CALENDAR,"4986e7","3f51b5","7577c4"),
  CalendarColor.LAVANDE : GoogleCalendarColor("Lavande"        ,ColorType.COLOR_TYPE_CALENDAR,"9a9cff","7986cb","818db0"),
  CalendarColor.GLYCINE : GoogleCalendarColor("Glycine"        ,ColorType.COLOR_TYPE_CALENDAR,"b99aff","b39ddb","aa9ccb"),
  CalendarColor.AMETHYSTE : GoogleCalendarColor("Amethyste"    ,ColorType.COLOR_TYPE_CALENDAR,"a47ae2","9e69af","a07bae"),
  CalendarColor.RAISIN : GoogleCalendarColor("Raison"          ,ColorType.COLOR_TYPE_CALENDAR,"cd74e6","8e24aa","aa60b6"),
  CalendarColor.CACAO : GoogleCalendarColor("Cacao"            ,ColorType.COLOR_TYPE_CALENDAR,"ac725e","795548","977765"),
  CalendarColor.ANTHRACITE : GoogleCalendarColor("Anthracite"  ,ColorType.COLOR_TYPE_CALENDAR,"c2c2c2","616161","818181"),
  CalendarColor.GRIS_TAUPE : GoogleCalendarColor("Gris Taupe"  ,ColorType.COLOR_TYPE_CALENDAR,"cabdbf","a79b8e","a8988a"),
}

event_color_list = {
  EventColor.FLAMANT_ROSE : GoogleCalendarColor("Flamant Rose" ,ColorType.COLOR_TYPE_CALENDAR,"ffb878","e67c73","d58476"),
  EventColor.TOMATE : GoogleCalendarColor("Tomate"             ,ColorType.COLOR_TYPE_CALENDAR,"dc2127","d50000","dd583e"),
  EventColor.BANANE : GoogleCalendarColor("Banane"             ,ColorType.COLOR_TYPE_CALENDAR,"fbd75b","f6bf26","e6bd56"),
  EventColor.MANDARINE : GoogleCalendarColor("Mandarine"       ,ColorType.COLOR_TYPE_CALENDAR,"ff887c","f4511e","e56946"),
  EventColor.SAUGE : GoogleCalendarColor("Sauge"               ,ColorType.COLOR_TYPE_CALENDAR,"51b749","0b8043","59ad7f"),
  EventColor.BASILIC : GoogleCalendarColor("Basilic"           ,ColorType.COLOR_TYPE_CALENDAR,"7ae7bf","33b679","4c9564"),
  EventColor.MYRTILLE : GoogleCalendarColor("Myrtille"         ,ColorType.COLOR_TYPE_CALENDAR,"5484ed","3f51b5","7577c4"),
  EventColor.PAON : GoogleCalendarColor("Paon"                 ,ColorType.COLOR_TYPE_CALENDAR,"46d6db","039be5","519bcd"),
  EventColor.RAISIN : GoogleCalendarColor("Raisin"             ,ColorType.COLOR_TYPE_CALENDAR,"dbadff","8e24aa","ab60ba"),
  EventColor.LAVANDE : GoogleCalendarColor("Lavande"           ,ColorType.COLOR_TYPE_CALENDAR,"a4bdfc","7986cb","838cc1"),
  # Default calendar color goes here
  EventColor.GRAPHITE : GoogleCalendarColor("Graphite"         ,ColorType.COLOR_TYPE_CALENDAR,"e1e1e1","616161","807f7e"),
}