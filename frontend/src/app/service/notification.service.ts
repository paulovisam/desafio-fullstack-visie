import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {
    
    constructor(
        private toastr: ToastrService
    ) { }

    public info(message: string | undefined, title?: string | undefined) {
        this.toastr.info(message,title,{
            "progressBar": true,
            "timeOut": 2500,
        });
    }
    public warning(message: string | undefined, title?: string | undefined) {
        this.toastr.warning(message,title,{
            "progressBar": true,
            "timeOut": 2500,
        });
    }
    public success(message: string | undefined, title?: string | undefined) {
        this.toastr.success(message,title,{
            "progressBar": true,
            "timeOut": 2500,
        });
    }
    public error(message: string | undefined, title?: string | undefined) {
        this.toastr.error(message,title,{
            "progressBar": true,
            "timeOut": 2500,
        });
    }
}