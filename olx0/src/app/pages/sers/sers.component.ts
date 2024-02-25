import { HttpClient } from '@angular/common/http';
import { Component,OnInit } from '@angular/core';
import { trigger, state, style, transition, animate } from '@angular/animations';
import { FormBuilder, FormGroup } from '@angular/forms';
import { DomSanitizer,SafeResourceUrl } from '@angular/platform-browser';


@Component({
  selector: 'app-sers',
  templateUrl: './sers.component.html',
  styleUrls: ['./sers.component.css'],
  animations: [
    trigger('formAnimation', [
      state('void', style({ opacity: 0, transform: 'translateY(-20px)' })),
      transition('void => *', animate('300ms ease-in')),
      transition('* => void', animate('300ms ease-out')),
    ]),
  ],
})
export class SersComponent implements OnInit {
  iframeUrls: { [key: string]: SafeResourceUrl } = {};

  public jsonData: any;
  public showForm: boolean = false;
  updateForm!: FormGroup;

  public model: string = '';
  public price_hight: number = 0;
  public price_low: number = 0;
  public use: number = 0;
  public city: string = '';



  public showModelInput: boolean = false;
  public showPriceHightInput: boolean = false;
  public showPriceLowInput: boolean = false;
  public showUseInput: boolean = false;
  public showCityInput: boolean = false;


  constructor(private formBuilder: FormBuilder, private http: HttpClient,  private domSanitizer: DomSanitizer){

  this.updateForm = this.formBuilder.group({
    model: [''],
    price_hight: [0],
    price_low: [0],
    use: [0],
    city: [''],
  });
  }

  ngOnInit(): void {

    this.getMethod();
  }



  public getMethod(){
    this.http.get('http://127.0.0.1:8000/get_item_search/').subscribe((data) =>{
      console.log(data);
      this.jsonData = data;
    }
    );
  }
  public submitForm() {

    const formData = {
      model: this.model,
      price_hight: this.price_hight,
      price_low: this.price_low,
      use: this.use,
      city: this.city
      // Add other fields
    };

    this.http.post('http://127.0.0.1:8000/fer/', formData).subscribe(
      (response) => {
        console.log('Post request successful', response);
        // Handle success, if needed
      },
      (error) => {
        console.error('Error in post request', error);
        // Handle error, if needed
      }
    );
  }
  public putMethod(id: string){
    const formData = {
      model: this.updateForm.get('model')?.value,
      price_hight: this.updateForm.get('price_hight')?.value,
      price_low: this.updateForm.get('price_low')?.value,
      use: this.updateForm.get('use')?.value,
      city: this.updateForm.get('city')?.value,
    };
    this.http.put(`http://127.0.0.1:8000/${id}`, formData).subscribe(
      (response) =>{
        console.log('Put reques seccessful', response);
      },
      (error) => {
        console.error('Error in put request', error);
      }
    );
  }
  public deleteMethod(id: string){
    this.http.delete(`http://127.0.0.1:8000/${id}_item/`).subscribe(
        (response) => {
            console.log('Delete request successful', response);
            // Handle success, if needed
        },
        (error) => {
            console.error('Error in delete request', error);
            // Handle error, if needed
        }
    );
  }
  

  public runAction(id: string) {
    this.http.post('http://127.0.0.1:8000/save_link_on_olx/', { id }).subscribe(response => {
      console.log(response);
      // Handle response, e.g., show a message to the user
      this.updateIframeSrc('/animat/', id);
    });
  }

  public async stopAction(id: string) {
    try {
        await this.http.post('http://127.0.0.1:8000/stop_processing/', { id }).toPromise();
        console.log("Processing stopped successfully for item with ID:", id);
        this.updateIframeSrc('', id);
    } catch (error) {
        console.error("Error stopping processing for item with ID:", id, error);
    }
  }

  toggleFormElements() {

    this.showModelInput = !this.showModelInput;
    this.showPriceHightInput = !this.showPriceHightInput;
    this.showPriceLowInput = !this.showPriceLowInput;
    this.showUseInput = !this.showUseInput;
    this.showCityInput = !this.showCityInput;
  }
  showFormPost(){
    this.showForm = !this.showForm;
  }
  updateIframeSrc(newUrl: string, id: string){
    this.iframeUrls[id] = this.domSanitizer.bypassSecurityTrustResourceUrl(newUrl)
  }
}