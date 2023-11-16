import { Component, OnInit } from '@angular/core';
import { PeopleService } from 'src/app/service/people/people.service';
import { NotificationService } from 'src/app/service/notification.service';
import { PersonView } from 'src/app/view/PersonView';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  
  public people!: PersonView[];

  public showDeleteModal:boolean = false;
  public personDelete: PersonView = {};

  public showCreateModal:boolean = false;
  public personCreate: PersonView = {};

  public showUpdateModal:boolean = false;
  public personUpdate: PersonView = {};

  public showInfoModal:boolean = false;
  public personInfo: PersonView = {};

  ngOnInit(): void {
    this.people = [];
    this.peopleService.read().subscribe({
      next: (people) => {
        for(const person of people) {
          person.nome_abv = person.nome?.split(" ")[0];

          let date: undefined | string[] = person.data_admissao?.split("-");
          if(date != undefined) {
            person.data_admissao_br = date[2]+"/"+date[1]+"/"+date[0];
          }
          this.people.push(person)
        }
        
      }
    });
  }

  constructor(
    private peopleService: PeopleService,
    private notificationService: NotificationService
  ) {}

  public deletePersonSelect(person: PersonView) {
    this.showDeleteModal = true;
    this.personDelete = person;
  }
  public deletePersonSend() {
    if(this.personDelete.cpf) {
      this.peopleService.deleteByCPF(this.personDelete.cpf).subscribe({
        next: (data)=> {
          this.notificationService.success("Funcionário apagado!")
          for(let i = 0; i < this.people.length; i++) {
            if(this.people[i].cpf == this.personDelete.cpf) {
              this.people.splice(i,1);
              break;
            }
          }
        },
        error: (err) => {
          this.notificationService.error("Falha ao apagar funcionário");
        }
      })
    }
    this.showInfoModal = false;
    this.showDeleteModal = false;
  }
  public deletePersonCancel() {
    this.showDeleteModal = false;
  }
  
  public createPersonSelect() {
    this.showCreateModal = true;
  }
  public createPersonSend() {
    this.peopleService.create(this.personCreate).subscribe({
      next: (data) => {
        this.notificationService.success("Funcionário criado com sucesso!")
        data.nome_abv = data.nome?.split(" ")[0];

        let date: undefined | string[] = data.data_admissao?.split("-");
        if(date != undefined) {
          data.data_admissao_br = date[2]+"/"+date[1]+"/"+date[0];
        }
        
        this.people.push(data)
        this.personCreate = {}
      },
      error: (err) => {
        this.notificationService.error("Falha ao criar funcionário");
      }
    })
    
    this.showCreateModal = false;
  }
  public createPersonCancel() {
    this.showCreateModal = false;
  }
  
  public updatePersonSelect(person: PersonView) {
    this.showUpdateModal = true;
    this.personUpdate = person;
  }
  public updatePersonSend() {
    this.peopleService.update(this.personUpdate).subscribe({
      next: (data) => {
        for(let i = 0; i < this.people.length; i++) {
          if(this.people[i].id_pessoa == this.personUpdate.id_pessoa) {
            this.notificationService.success("Dados atualizados com sucesso!")
            data.nome_abv = data.nome?.split(" ")[0];
            let date: undefined | string[] = data.data_admissao?.split("-");
            if(date != undefined) {
              data.data_admissao_br = date[2]+"/"+date[1]+"/"+date[0];
            }
            this.people[i] = data;
            break;
          }
        }
      },
      error: (err) => {
        this.notificationService.error("Falha ao atualizar dados");
      }
    });

    this.showUpdateModal = false;
  }
  public updatePersonCancel() {
    this.showUpdateModal = false;
  }
  
  public infoPersonSelect(person: PersonView) {
    this.showInfoModal = true;
    if(person.id_pessoa) {
      this.peopleService.readById(person.id_pessoa).subscribe({
        next: (data) => {
          this.notificationService.info("Dados obtidos com sucesso!");
          this.personInfo = data;
        },
        error: (err) => {
          this.notificationService.error("Falha ao obter dados");
        }
      })
    }
  }
  public infoPersonClose() {
    this.showInfoModal = false;
  }
}
