import { HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnvironmentService {
    private production: boolean = true;

    constructor(
    ) { }

    public getEnvironment() {
      if(this.production) {
        return "http://144.22.220.135:8000/api/v1";
      } else {
        return "http://localhost:8000/api/v1";
      }
    }

    public getOptions() {
      const httpOptions = {
        headers: new HttpHeaders({
          'Content-Type':  'application/json'
        })
      };
      return httpOptions;
    }

}