import console from 'console'
import produceList from './lib/FruitAndVegetable.json'

export default function (input) {
  const { produceName, season } = input

  let message = "No"

  for (let i = 0; i < produceList.length; i++) {

    if (produceList[i].name.toLowerCase() == produceName.toLowerCase()) {
      for (let j = 0; j < produceList[i].season.length; j++) {
        if (season == produceList[i].season[j]) {
          message = "Yes"
          break
        }
      }
      break
    }
  }
  return message
}