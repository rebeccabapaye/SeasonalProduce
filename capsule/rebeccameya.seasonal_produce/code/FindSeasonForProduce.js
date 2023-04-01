import console from 'console'
import produceList from './lib/FruitAndVegetable.json'

export default function (input) {
  let season = "Not Found";

  for (var i = 0; i < produceList.length; i++) {
    console.log(produceList[i].name.toLowerCase())

    if (produceList[i].name.toLowerCase() == input.produceName.toLowerCase()) {
      console.log(produceList[i])
      season = produceList[i].season
    }
  }
  return season
}