# Google Calendar Color
Colors used by google in its calendar app

## Why ?
It looks like there's no way in the API to get a clear definition of colors used in Google Calendar.

Google is also using different colors depending on the platform.

## What this python covers
- Calendar colors and event colors
- ColorId can be retrived from the CalendarColor and EventColor enums
- calendar_color_list and event_color_list list all colors in the order of the android app
- For each color, you have
  - color_name: In case you need to display it
  - color_type: COLOR_TYPE_CALENDAR / COLOR_TYPE_EVENT
  - api_color: Color returned by the api
  - web_color: Color used on https://calendar.google.com/
  - android_color: Color used on the android app
- 2 versions available : English and French

 ## Thanks to 
 ansaso that listed all the colorIds https://gist.github.com/ansaso/accaddab0892a3b47d5f4884fda0468b
