import console from 'console'
import produceList from './lib/FruitAndVegetable.json'

export default function (input) {
  let season = "Not Found"

  for (let i = 0; i < produceList.length; i++) {

    if (produceList[i].name.toLowerCase() == input.produceName.toLowerCase()) {
      console.log(produceList[i])
      season = produceList[i].season
      break
    }
  }
  return season
}