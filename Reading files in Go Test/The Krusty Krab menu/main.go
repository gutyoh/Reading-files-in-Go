package main

import (
    "fmt"
    "io/ioutil"
)

func main() {
    file, err := ioutil.ReadFile("galley_grub.txt") // open the file here with the ioutil.ReadFile() function
    if err != nil {
        fmt.Println(err) // exit if we have an error
    }
    fmt.Println(string(file))
}