function cal_to_gsht_multi(){

  var ss = SpreadsheetApp.openById( '__id here__' ), // Id is set to file 'CAL-to-gsheets' in LPRMF dir
      sheet = ss.getActiveSheet(),
      cals = ['mail1@domain', 'mail2@domain'], c, cal, calName,
      
 //??     cals = getAllCalendars(),
    
      today = new Date(),
      start = new Date( today ), end = new Date( 'Dec 31, 2019' ),
      events, i, details,
      eventslog = [], e,
      rows = [], range;
  
  sheet.clearContents();  
  
  for (c = 0; c < cals.length; c += 1) {

    cal = CalendarApp.getCalendarById(cals[c]);
    calName = cal.getTitle();
    events = cal.getEvents(start, end);

    // add the events of the current calendar to the array of all events
    eventslog = eventslog.concat(
      events.map(function(event) {  
        return {
          time: new Date(event.getStartTime()).getTime(), // sort by this
          details: [
            calName, // calNAme-change calendar info position in array to adjust
            event.getTitle(),
            event.getDescription(),
            event.getLocation(),
            event.getStartTime(),
            event.getEndTime(),
            event.getGuestList().map(function(x) {return x.getEmail();}).join(',')
          ]
        };
      })
    );
  }

  // sort array of event so date order can be either way by reversing a & b
  eventslog.sort(function(a, b) { return a.time - b.time; });

  rows = eventslog.map(function(entry) { return entry.details; });

  range = sheet.getRange(2, 1, rows.length, 7);  // no. of event.details ; increase if more event.get
  range.setValues(rows);
}
