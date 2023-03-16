import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { environment } from '../class/environment'
import { Response } from '../class/response';

@Injectable({
  providedIn: 'root'
})
export class PiecesService {
  constructor(private http: HttpClient) {
  }

  url = environment.apiUrl
  
  getData() {
    return this.http.get<Response>(this.url)
  }

  makeMove(move: string) {
    return this.http.get<Response>(this.url+'api/move/'+move)
  }
}