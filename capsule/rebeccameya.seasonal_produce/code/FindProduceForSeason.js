import console from 'console'
import produceList from './lib/FruitAndVegetable.json'

export default function (input) {

  let produce = []

  for (let i = 0; i < produceList.length; i++) {
    if (input.produceType) {
      if (produceList[i].type.toLowerCase() === input.produceType.toLowerCase()) {
        for (let j = 0; j < produceList[i].season.length; j++) {
          if (produceList[i].season[j].toLowerCase() === input.season.toLowerCase()) {
            produce.push(produceList[i])
            break
          }
        }
      }
    } else {
      for (let j = 0; j < produceList[i].season.length; j++) {
        if (produceList[i].season[j].toLowerCase() === input.season.toLowerCase()) {
          produce.push(produceList[i])
          break
        }
      }
    }
  }
  // Return produce
  return produce
}
