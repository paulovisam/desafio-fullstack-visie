import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { EnvironmentService } from '../environment.service';
import { PersonView } from 'src/app/view/PersonView';

@Injectable({
    providedIn: 'root'
  })
export class PeopleService {

    constructor(
        private http: HttpClient,
        private environmentService: EnvironmentService
    ) { }
    
    public create(personView: PersonView): Observable<PersonView> {
        return this.http.post<PersonView>(this.environmentService.getEnvironment() + '/people', personView);
    }
    public read(): Observable<PersonView[]> {
        return this.http.get<PersonView[]>(this.environmentService.getEnvironment() + '/people');
    }
    public readById(id: number): Observable<PersonView> {
        return this.http.get<PersonView>(this.environmentService.getEnvironment() + '/people?id=' + id);
    }
    public readByCPF(cpf: string): Observable<PersonView> {
        return this.http.get<PersonView>(this.environmentService.getEnvironment() + '/people?cpf=' + cpf);
    }
    public readByRG(rg: string): Observable<PersonView> {
        return this.http.get<PersonView>(this.environmentService.getEnvironment() + '/people?rg=' + rg);
    }
    public update(personView: PersonView): Observable<PersonView> {
        return this.http.put<PersonView>(this.environmentService.getEnvironment() + '/people', personView);
    }
    public deleteById(id: number): Observable<PersonView> {
        return this.http.delete<PersonView>(this.environmentService.getEnvironment() + '/people?id=' + id);
    }
    public deleteByCPF(cpf: string): Observable<PersonView> {
        return this.http.delete<PersonView>(this.environmentService.getEnvironment() + '/people?cpf=' + cpf);
    }
    public deleteByRG(rg: string): Observable<PersonView> {
        return this.http.delete<PersonView>(this.environmentService.getEnvironment() + '/people?rg=' + rg);
    }
}