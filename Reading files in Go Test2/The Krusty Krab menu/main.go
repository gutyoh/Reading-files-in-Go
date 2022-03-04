package main

import (
    "fmt"
    "io/ioutil"
    "log"
)

func main() {
    file, err := ? // open the file here with the ioutil.ReadFile() function
    if err != nil {
        log.Println(err) // print the error in case there is any
    }
    // print the contents of the file here as a 'string'
    fmt.Println(?)
}