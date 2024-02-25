import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

interface YourDataType {
  items_search_id: string;
  name_url: string;
  price_url: string;
  meet_url: string;
  url: string;
  // Add other properties if needed
}

@Component({
  selector: 'app-analiz',
  templateUrl: './analiz.component.html',
  styleUrls: ['./analiz.component.css'],
})
export class AnalizComponent implements OnInit {
  public jsonData: YourDataType[] = [];
  public modelFilter: string = '';
  public forSearchFilter: string = '';
  public searchData: string = '';
  public sortDirection: string = 'min'; // Initial sorting direction

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getMethod();
  }

  public getMethod() {
    this.http.get<YourDataType[]>('http://127.0.0.1:8000/get_save_link/').subscribe((data) => {
      console.log(data);
      this.jsonData = data;
      this.sortData(); // Optionally sort data after fetching
    });
  }

  public toggleSortDirection() {
    // Toggle sorting direction between 'asc' and 'desc'
    this.sortDirection = this.sortDirection === 'min' ? 'max' : 'min';
    this.sortData();
  }

  public sortData() {
    // Sort jsonData based on the price column
    this.jsonData.sort((a, b) => {
      const priceA = parseFloat(a.price_url);
      const priceB = parseFloat(b.price_url);

      if (this.sortDirection === 'min') {
        return priceA - priceB;
      } else {
        return priceB - priceA;
      }
    });
  }
}
