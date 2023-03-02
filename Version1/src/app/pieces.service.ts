import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class PiecesService {
  constructor(private http: HttpClient) { }
  getData() {
    let url = "http://127.0.0.1:5000/"
    return this.http.get(url)
  }
}
