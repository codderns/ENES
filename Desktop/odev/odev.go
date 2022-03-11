package main

import (
	"fmt"
	"sort"
)

type Books struct {
	Name string
}

func main() {
	lt := []Books{{"LOTR"}, {"GOT"}, {"LOST"}}

	sort.Slice(lt, func(i, j int) bool {
		return lt[i].Name <= lt[j].Name
	})

	var searchb string
	fmt.Scanf(searchb)
	fmt.Printf("Searched: %v \n", searchb)
	x := sort.Search(len(lt), func(i int) bool {
		return string(lt[i].Name) >= searchb
	})
	if x < len(lt) && lt[x].Name == searchb {
		fmt.Println("FOUND")
	} else {
		fmt.Println("NOT FOUND", x)
	}

}
