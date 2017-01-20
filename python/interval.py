Initially set R be the set of all requests, and let A be empty
While R is not yet empty
  Choose a request i from R that has the smallest finishing time
  Add request i to A
  Delete all requests from R that are not compatible with request i
Return the set A as the set of accepted requests

