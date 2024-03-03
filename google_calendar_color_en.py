from enum import Enum

class ColorType(Enum):
  COLOR_TYPE_CALENDAR = 0
  COLOR_TYPE_EVENT = 0

class CalendarColor(Enum):
  COCOA = 1
  FLAMINGO = 2
  TOMATO = 3
  TANGERINE = 4
  PUMKIN = 5
  MANGO = 6
  EUCALYPTUS = 7
  BASIL = 8
  PISTACHIO = 9
  AVOCADO = 10
  CITRON = 11
  BANANA = 12
  SAGE = 13
  PEACOCK = 14
  COBALT = 15
  BLUEBERRY = 16
  LAVENDER = 17
  WISTERIA = 18
  GRAPHITE = 19
  BIRCH = 20
  BEETROOT = 21
  CHERRY_BLOSSOM = 22
  GRAPE = 23
  AMETHYST = 24
  
class EventColor(Enum):
  LAVENDER = 1
  SAGE = 2
  GRAPE = 3
  FLAMINGO = 4
  BANANA = 5
  TANGERINE = 6
  PEACOCK = 7
  GRAPHITE = 8
  BLUEBERRY = 9
  BASIL = 10
  TOMATO = 11

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
  CalendarColor.BEETROOT : GoogleCalendarColor("Beetroot"             ,ColorType.COLOR_TYPE_CALENDAR,"ac725e","ad1457","c25978"),
  CalendarColor.CHERRY_BLOSSOM : GoogleCalendarColor("Cherry Blossom" ,ColorType.COLOR_TYPE_CALENDAR,"cca6ac","d81b60","dd5c7a"),
  CalendarColor.TOMATO : GoogleCalendarColor("Tomato"                 ,ColorType.COLOR_TYPE_CALENDAR,"f83a22","d50000","d8583b"),
  CalendarColor.FLAMINGO : GoogleCalendarColor("Flamingo"             ,ColorType.COLOR_TYPE_CALENDAR,"f691b2","e67c73","d4847b"),
  CalendarColor.TANGERINE : GoogleCalendarColor("Tangering"           ,ColorType.COLOR_TYPE_CALENDAR,"fa573c","f4511e","e16c41"),
  CalendarColor.PUMKIN : GoogleCalendarColor("Punkin"                 ,ColorType.COLOR_TYPE_CALENDAR,"ff7537","ef6c00","dc7b3a"),
  CalendarColor.MANGO : GoogleCalendarColor("Mango"                   ,ColorType.COLOR_TYPE_CALENDAR,"ffad49","f09300","de9540"),
  CalendarColor.BANANA : GoogleCalendarColor("Banana"                 ,ColorType.COLOR_TYPE_CALENDAR,"fac165","f6bf26","e8bb5c"),
  CalendarColor.CITRON : GoogleCalendarColor("Citron"                 ,ColorType.COLOR_TYPE_CALENDAR,"fbe983","eac441","e6bb57"),
  CalendarColor.AVOCADO : GoogleCalendarColor("Avocado"               ,ColorType.COLOR_TYPE_CALENDAR,"b3dc6c","c0ca33","bec058"),
  CalendarColor.PISTACHIO : GoogleCalendarColor("Pistachio"           ,ColorType.COLOR_TYPE_CALENDAR,"7bd148","7cb342","86a95c"),
  CalendarColor.SAGE : GoogleCalendarColor("Sage"                     ,ColorType.COLOR_TYPE_CALENDAR,"42d692","33b679","58ad87"),
  CalendarColor.BASIL : GoogleCalendarColor("Basil"                   ,ColorType.COLOR_TYPE_CALENDAR,"16a765","0b8043","4e9462"),
  CalendarColor.EUCALYPTUS : GoogleCalendarColor("Eucalyptus"         ,ColorType.COLOR_TYPE_CALENDAR,"92e1c0","009688","479b91"),
  CalendarColor.PEACOCK : GoogleCalendarColor("Peacock"               ,ColorType.COLOR_TYPE_CALENDAR,"9fe1e7","039be5","5498cf"),
  CalendarColor.COBALT : GoogleCalendarColor("Cobalt"                 ,ColorType.COLOR_TYPE_CALENDAR,"9fc6e7","4285f4","6c8cdc"),
  CalendarColor.BLUEBERRY : GoogleCalendarColor("blueberry"           ,ColorType.COLOR_TYPE_CALENDAR,"4986e7","3f51b5","7577c4"),
  CalendarColor.LAVENDER : GoogleCalendarColor("Lavender"             ,ColorType.COLOR_TYPE_CALENDAR,"9a9cff","7986cb","818db0"),
  CalendarColor.WISTERIA : GoogleCalendarColor("Wisteria"             ,ColorType.COLOR_TYPE_CALENDAR,"b99aff","b39ddb","aa9ccb"),
  CalendarColor.AMETHYST : GoogleCalendarColor("Amethyst"             ,ColorType.COLOR_TYPE_CALENDAR,"a47ae2","9e69af","a07bae"),
  CalendarColor.GRAPE : GoogleCalendarColor("Grape"                   ,ColorType.COLOR_TYPE_CALENDAR,"cd74e6","8e24aa","aa60b6"),
  CalendarColor.COCOA : GoogleCalendarColor("Cocoa"                   ,ColorType.COLOR_TYPE_CALENDAR,"ac725e","795548","977765"),
  CalendarColor.GRAPHITE : GoogleCalendarColor("Graphite"             ,ColorType.COLOR_TYPE_CALENDAR,"c2c2c2","616161","818181"),
  CalendarColor.BIRCH : GoogleCalendarColor("Birch"                   ,ColorType.COLOR_TYPE_CALENDAR,"cabdbf","a79b8e","a8988a"),
}

event_color_list = {
  EventColor.FLAMINGO : GoogleCalendarColor("Flamingo"        ,ColorType.COLOR_TYPE_CALENDAR,"ffb878","e67c73","d58476"),
  EventColor.TOMATO : GoogleCalendarColor("Tomato"            ,ColorType.COLOR_TYPE_CALENDAR,"dc2127","d50000","dd583e"),
  EventColor.BANANA : GoogleCalendarColor("Banana"            ,ColorType.COLOR_TYPE_CALENDAR,"fbd75b","f6bf26","e6bd56"),
  EventColor.TANGERINE : GoogleCalendarColor("Tangerine"      ,ColorType.COLOR_TYPE_CALENDAR,"ff887c","f4511e","e56946"),
  EventColor.SAGE : GoogleCalendarColor("Sage"                ,ColorType.COLOR_TYPE_CALENDAR,"51b749","0b8043","59ad7f"),
  EventColor.BASIL : GoogleCalendarColor("Basil"              ,ColorType.COLOR_TYPE_CALENDAR,"7ae7bf","33b679","4c9564"),
  EventColor.BLUEBERRY : GoogleCalendarColor("Blueberry"      ,ColorType.COLOR_TYPE_CALENDAR,"5484ed","3f51b5","7577c4"),
  EventColor.PEACOCK : GoogleCalendarColor("Peacock"          ,ColorType.COLOR_TYPE_CALENDAR,"46d6db","039be5","519bcd"),
  EventColor.GRAPE : GoogleCalendarColor("Grape"              ,ColorType.COLOR_TYPE_CALENDAR,"dbadff","8e24aa","ab60ba"),
  EventColor.LAVENDER : GoogleCalendarColor("Lavender"        ,ColorType.COLOR_TYPE_CALENDAR,"a4bdfc","7986cb","838cc1"),
  # Default calendar color goes here
  EventColor.GRAPHITE : GoogleCalendarColor("Graphite"        ,ColorType.COLOR_TYPE_CALENDAR,"e1e1e1","616161","807f7e"),
}