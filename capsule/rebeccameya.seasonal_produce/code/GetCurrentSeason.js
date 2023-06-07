import console from 'console'

export default function () {

  let currentDate = new Date()
  let currentMonth = currentDate.getMonth()
  console.log("Current Date: " + currentDate)
  console.log("Current Month: " + currentMonth)

  let currentSeason = null

  if (currentMonth >= 2 && currentMonth <= 4)
    currentSeason = "Spring"
  else if (currentMonth >= 5 && currentMonth <= 7)
    currentSeason = "Summer"
  else if (currentMonth >= 8 && currentMonth <= 10)
    currentSeason = "Fall"
  else
    currentSeason = "Winter"

console.log("Current Season: " + currentSeason)

return currentSeason
}


// 0 Jan
// 1 Feb
// 2 Mar
// 3 Apr
// 4 May
// 5 Jun
// 6 Jul
// 7 Aug
// 8 Sep
// 9 Oct
// 10 Nov
// 11 Dec